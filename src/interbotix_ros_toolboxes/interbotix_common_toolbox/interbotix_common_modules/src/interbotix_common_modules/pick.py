import sys
import copy
import rospy
import moveit_commander
import geometry_msgs.msg
from tf.transformations import quaternion_from_euler
import tf2_ros

from math import radians, degrees
from moveit_msgs.msg import DisplayTrajectory
from geometry_msgs.msg import Quaternion

class MoveGroupPythonInterfaceTutorial(object):
    def __init__(self):
        super(MoveGroupPythonInterfaceTutorial, self).__init__()
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('moveit_python_interface')

        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        self.arm_group = moveit_commander.MoveGroupCommander("interbotix_arm")
        self.gripper_group = moveit_commander.MoveGroupCommander("interbotix_gripper")  # Gripper control
        self.display_trajectory_publisher = rospy.Publisher('move_group/display_planned_path',
                                                            DisplayTrajectory,
                                                            queue_size=20)

        self.planning_frame = self.arm_group.get_planning_frame()
        self.eef_link = self.arm_group.get_end_effector_link()
        self.group_names = self.robot.get_group_names()
        # Set the planner to RRTStar
        self.set_planner('RRTstarkConfigDefault')
        self.arm_group = moveit_commander.MoveGroupCommander("interbotix_arm")
        self.arm_group.set_max_velocity_scaling_factor(0.5)  # Adjust as necessary
        self.arm_group.set_max_acceleration_scaling_factor(0.5)  # Adjust as necessary
        self.tfBuffer = tf2_ros.Buffer()
        
    def all_close(self, goal, actual, tolerance=0.05):
        if type(goal) is list:
            for index in range(len(goal)):
                if abs(actual[index] - goal[index]) > tolerance:
                    return False
        elif type(goal) is geometry_msgs.msg.PoseStamped:
            return self.all_close([goal.pose.position.x, goal.pose.position.y, goal.pose.position.z,
                                   goal.pose.orientation.x, goal.pose.orientation.y, goal.pose.orientation.z, goal.pose.orientation.w],
                                  [actual.pose.position.x, actual.pose.position.y, actual.pose.position.z,
                                   actual.pose.orientation.x, actual.pose.orientation.y, actual.pose.orientation.z, actual.pose.orientation.w], tolerance)
        elif type(goal) is geometry_msgs.msg.Pose:
            return self.all_close([goal.position.x, goal.position.y, goal.position.z,
                                   goal.orientation.x, goal.orientation.y, goal.orientation.z, goal.orientation.w],
                                  [actual.position.x, actual.position.y, actual.position.z,
                                   actual.orientation.x, actual.orientation.y, actual.orientation.z, actual.orientation.w], tolerance)
        return True
    
    def set_planner(self, planner_id):
        """ Set the planner ID for planning """
        self.arm_group.set_planner_id(planner_id)

    def go_to_joint_state(self):
        ## Planning to a Joint Goal
        ## ^^^^^^^^^^^^^^^^^^^^^^^^

        print("============ Printing Joint Goal: " + str(self.joint_goal))

        # The go command can be called with joint values, poses, or without any
        # parameters if you have already set the pose or joint target for the group
        self.arm_group.go(self.joint_goal, wait=True)

        # Calling ``stop()`` ensures that there is no residual movement
        self.arm_group.stop()

        current_joints = self.arm_group.get_current_joint_values()
        return self.all_close(self.joint_goal, current_joints, 0.01)
    
    def gripper_open(self):
        """Open the gripper using predefined joint values."""
        gripper_joint_values = [0.037, -0.037]  # Corresponds to the 'Open' state in SRDF
        self.gripper_group.go(gripper_joint_values, wait=True)
        self.gripper_group.stop()  # Ensure no residual movement

    def gripper_close(self):
        """Close the gripper using predefined joint values."""
        gripper_joint_values = [0.015, -0.015]  # Corresponds to the 'Closed' state in SRDF
        self.gripper_group.go(gripper_joint_values, wait=True)
        self.gripper_group.stop()  # Ensure no residual movement

    def add_collision_object(self,object_ee_goal=(0.0, 0.2, 0.1)):
        # Define the size and pose of the box
        #box_size = (0.3, 0.05, 0.3)  # Dimensions of the box (width, depth, height)
        box_size = (0.1, 0.1, 0.1)
        box_pose = geometry_msgs.msg.PoseStamped()
        box_pose.header.frame_id = "world" #self.planning_frame
        box_pose.pose.orientation.w = 1.0
        box_pose.pose.position.x = object_ee_goal[0]-0.00
        box_pose.pose.position.y = object_ee_goal[1]+0.00
        box_pose.pose.position.z = 0.01 + box_size[2] / 2  # Position at half the height to sit on the plane

        # Use the correct method to add a box to the planning scene
        self.scene.add_box("big_box1", box_pose, box_size)
        rospy.sleep(1)  # Allow time for the addition to be processed


    def add_box(self, object_ee_goal=(0.3, 0.05, 0.25), bias_angle = radians(0), timeout=4):
        box_pose = geometry_msgs.msg.PoseStamped()
        box_pose.header.frame_id = "world"
        box_pose.pose.position.x = object_ee_goal[0]
        box_pose.pose.position.y = object_ee_goal[1]
        box_pose.pose.position.z = object_ee_goal[2]
        quat = quaternion_from_euler(0, 0, bias_angle)  # 30 degrees Z
        # Correctly assign quaternion values to a Quaternion message
        box_pose.pose.orientation = Quaternion(*quat)

        self.box_name = "box"
        self.scene.add_box(self.box_name, box_pose, size=(0.02, 0.02, 0.02))
        self.wait_for_state_update(box_is_known=True, timeout=timeout)

    def attach_box(self, timeout=4):
        grasping_group = 'interbotix_gripper'
        touch_links = self.robot.get_link_names(group=grasping_group)
        self.scene.attach_box(self.arm_group.get_end_effector_link(), self.box_name, touch_links=touch_links)
        self.wait_for_state_update(box_is_attached=True, timeout=timeout)

    def detach_box(self, timeout=4):
        self.scene.remove_attached_object(self.arm_group.get_end_effector_link(), name=self.box_name)
        self.wait_for_state_update(box_is_attached=False, timeout=timeout)

    def remove_box(self, timeout=4):
        self.scene.remove_world_object(self.box_name)
        self.wait_for_state_update(box_is_known=False, timeout=timeout)

    def plan_cartesian_path_to_pick_box(self, object_ee_goal=(0.40, 0.03, 0.3), bias = 0):
        # Increase planning time
        self.arm_group.set_planning_time(10.0)
    
        # Determine the direction based on the bias input
        if bias == 0:
            bias_angle = radians(0)
        elif bias == 1: # Bias to the right
            bias_angle = radians(15)
        else:           # Bias to the left     
            bias_angle = radians(-15)



        waypoints = []
        # Start with the current end-effector pose
        start_pose = self.arm_group.get_current_pose().pose
        waypoints.append(copy.deepcopy(start_pose))

        # Create the goal pose directly without intermediate steps
        goal_pose = copy.deepcopy(start_pose)
        goal_pose.position.x = object_ee_goal[0]
        goal_pose.position.y = object_ee_goal[1]
        goal_pose.position.z = object_ee_goal[2]
        quat = quaternion_from_euler(0, 0, bias_angle)  # 30 degrees rotation around Z
        goal_pose.orientation = Quaternion(*quat)
        waypoints.append(copy.deepcopy(goal_pose))

        # Compute the Cartesian path
        (plan, fraction) = self.arm_group.compute_cartesian_path(
            waypoints,  # waypoints to follow
            0.01,       # eef_step
            0.0)        # jump_threshold - keep as zero for strict path following

        # Clear any existing path constraints to avoid affecting other operations
        rospy.loginfo("Trajectory details: %s", plan.joint_trajectory)
        self.arm_group.clear_path_constraints()
        rospy.sleep(1)  # Allow time for the robot to stabilize

        return plan, fraction

    def display_trajectory(self, plan):
        display_trajectory = DisplayTrajectory()
        display_trajectory.trajectory_start = self.robot.get_current_state()
        display_trajectory.trajectory.append(plan)
        self.display_trajectory_publisher.publish(display_trajectory)

    def execute_plan(self, plan):
        self.arm_group.execute(plan, wait=True)

    def wait_for_state_update(self, box_is_known=False, box_is_attached=False, timeout=4):
        start_time = rospy.get_time()
        current_time = rospy.get_time()
        while (current_time - start_time < timeout) and not rospy.is_shutdown():
            if box_is_known:
                is_known = self.box_name in self.scene.get_known_object_names()
                if is_known:
                    return True
            if box_is_attached:
                is_attached = len(self.scene.get_attached_objects([self.box_name])) > 0
                if is_attached:
                    return True
            rospy.sleep(0.1)
            current_time = rospy.get_time()
        return False
    
    def execute_plan(self, plan):
        # Ensure increasing timestamps
        last_time = 0.1  # start with a small offset if necessary
        for point in plan.joint_trajectory.points:
            point.time_from_start = rospy.Duration(last_time)
            last_time += 0.1  # increment to ensure each step increases; adjust the increment as necessary
        
        # Execute the trajectory
        self.arm_group.execute(plan, wait=True)
    
    def go_to_armtag_position(self):
        home_position = [0, -1, 1, 0, -1.5, 0]  # Example values
        self.arm_group.go(home_position, wait=True)
        rospy.sleep(1)  # Allow time for the robot to stabilize
        self.arm_group.stop()  # Ensure no residual movement

    def go_to_home_position(self):
        home_position = [0, 0, 0, 0, 0]  # Example values
        self.arm_group.go(home_position, wait=True)
        rospy.sleep(1)  # Allow time for the robot to stabilize
        self.arm_group.stop()  # Ensure no residual movement
    
    
    def rotate_wrist_joint(self, rotation_degrees=-60):
        rotation_radians = radians(rotation_degrees)
        current_joint_values = self.arm_group.get_current_joint_values()
        print("Current joint values:", current_joint_values)  # Debug print

        wrist_joint_index = -1  # Adjust as per your robot's configuration
        current_joint_values[wrist_joint_index] += rotation_radians
        print("Target joint values after rotation:", degrees(current_joint_values[-1]))  # Debug print

        # if current_joint_values[wrist_joint_index] < min_limit or current_joint_values[wrist_joint_index] > max_limit:
        #     print("Rotation out of bounds. Adjusting...")
            # Handle out-of-bounds target here

        self.arm_group.set_joint_value_target(current_joint_values)
        plan_success = self.arm_group.go(wait=True)
        return plan_success
    
    def go_to_sleep_pose(self):
        # Set the target to the named "Sleep" pose as defined in the robot's SRDF
        self.arm_group.set_named_target("Sleep")

        # Plan and execute the motion
        plan_success = self.arm_group.go(wait=True)
        self.arm_group.stop()  # Ensure there's no residual movement
        self.arm_group.clear_pose_targets()  # Clear targets after execution

        return plan_success
