import time
import colorsys
from interbotix_xs_modules.arm import InterbotixManipulatorXS
from interbotix_perception_modules.armtag import InterbotixArmTagInterface
from interbotix_perception_modules.pointcloud import InterbotixPointCloudInterface

# This script uses a color/depth camera to get the arm to find objects and pick them up.
# For this demo, the arm is placed to the left of the camera facing outward. When the
# end-effector is located at x=0, y=-0.3, z=0.2 w.r.t. the 'wx200/base_link' frame, the AR
# tag should be clearly visible to the camera. A small basket should also be placed in front of the arm.
#
# To get started, open a terminal and type 'roslaunch interbotix_xsarm_perception xsarm_perception.launch robot_model:=wx200'
# Then change to this directory and type 'python pick_place.py'

# determines the color of each object using the Hue value in the HSV color space

def main():
    # Initialize the arm module along with the pointcloud and armtag modules
    bot = InterbotixManipulatorXS("wx250s", moving_time=3, accel_time=0.75)
    pcl = InterbotixPointCloudInterface()
    armtag = InterbotixArmTagInterface()

    # get the ArmTag pose
    # bot.arm.set_ee_pose_components(x=0.02, z=0.4)
    # time.sleep(0.5)
    # bot.arm.set_ee_pose_components(y=-0.1, z=0.2)

    # time.sleep(0.5)
    # armtag.find_ref_to_arm_base_transform()
    # bot.arm.set_ee_pose_components(x=0, z=0)

    # get the cluster positions
    # sort them from max to min 'x' position w.r.t. the 'wx200/base_link' frame
    #TODO: get the world positions from realsense.py and set them as a list of coordinates here

    # set initial arm and gripper pose
    original_x, original_z = 0.02, 0.5
    bot.arm.set_ee_pose_components(x=original_x, z=original_z)
    bot.gripper.open()

    # pick up all the objects and drop them in a virtual basket in front of the robot
    #TODO: Loop through the world coordinates list and set the position of the arm based off of the specific position
    for cluster in world_positions:
        x, y, z = cluster
        print(cluster)
        x = min(x, 0.26)
        bot.arm.set_ee_pose_components(x=x, y=y-0.05, z=z, pitch=0.5)
        bot.arm.set_ee_pose_components(x=x, y=y-0.05, z=z, pitch=0.5)
        bot.gripper.set_pressure(1)
        bot.gripper.close()
        bot.arm.set_ee_pose_components(x=x, y=y-0.05, z=z, pitch=0.5)
        bot.arm.set_ee_pose_components(x=original_x, z=original_z)
        bot.gripper.open()



        # clr = color_compare(cluster["color"])
        # print(clr)
        # if (clr == "yellow"):
        #     bot.arm.set_ee_pose_components(x=0.2, y=-0.24, z=.2)
        # elif (clr == "orange"):
        #     bot.arm.set_ee_pose_components(x=0.2, y=-0.1, z=.2)
        # else:
        #     # if color cannot be recognized, then put the block back...
        #     bot.arm.set_ee_pose_components(x=x, y=y, z=z+0.08, pitch=0.5)
        # bot.gripper.open()
        # bot.arm.set_ee_pose_components(x=0.3, z=0.2)

    bot.arm.set_ee_pose_components(x=original_x, z=original_z)
    bot.arm.go_to_sleep_pose()

if __name__=='__main__':
    main()