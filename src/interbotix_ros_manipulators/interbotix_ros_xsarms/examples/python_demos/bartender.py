from interbotix_xs_modules.arm import InterbotixManipulatorXS
import numpy as np
import sys
from time import sleep

import threading


# This script makes the end-effector perform pick, pour, and place tasks
# Note that this script may not work for every arm as it was designed for the wx250
# Make sure to adjust commanded joint positions and poses as necessary
#
# To get started, open a terminal and type 'roslaunch interbotix_xsarm_control xsarm_control.launch robot_model:=wx250'
# Then change to this directory and type 'python bartender.py  # python3 bartender.py if using ROS Noetic'

def main():
    bot = InterbotixManipulatorXS("wx250s", "arm", "gripper")

    


    # joint_pwms = [100, 100 , 100, 125, 100, 100]
    # bot = InterbotixManipulatorXS("wx250s", "arm", "gripper")
    # bot.dxl.robot_set_operating_modes("group", "arm", "pwm")
    # bot.dxl.robot_write_commands("arm", joint_pwms)

    # joint_currents = [0, 200 , 200, 50, 0]
    # bot = InterbotixManipulatorXS(robot_model="wx250s")
    # bot.dxl.robot_set_operating_modes("group", "arm", "current")
    # bot.dxl.robot_write_commands("arm", joint_currents)


    if (bot.arm.group_info.num_joints < 5):
        print('This demo requires the robot to have at least 5 joints!')
        sys.exit()

    # bot.arm.set_ee_pose_components(x=0.3, z=0.2)
    # bot.arm.set_single_joint_position("waist", np.pi/2.0)
    # bot.gripper.open()
    # bot.arm.set_ee_cartesian_trajectory(x=0.1, z=-0.16)
    # bot.gripper.close()
    # bot.arm.set_ee_cartesian_trajectory(x=-0.1, z=0.16)
    # bot.arm.set_single_joint_position("waist", -np.pi/2.0)
    # bot.arm.set_ee_cartesian_trajectory(pitch=1.5)
    # bot.arm.set_ee_cartesian_trajectory(pitch=-1.5)
    # bot.arm.set_single_joint_position("waist", np.pi/2.0)
    # bot.arm.set_ee_cartesian_trajectory(x=0.1, z=-0.16)
    # bot.gripper.open()
    # bot.arm.set_ee_cartesian_trajectory(x=-0.1, z=0.16)
        
    # Define tasks to be run in parallel
    def open_gripper():
        bot.gripper.open()

    def set_ee_cartesian_trajectory():
        bot.arm.set_ee_cartesian_trajectory(x=-0.1, y=0.05, z=-0.2-0.121, pitch=1.5) #moving_time=None, wp_moving_time=0.85, wp_accel_time=0.5, wp_period=0.05)

        sleep(1.0)

    # Create threads
    gripper_thread = threading.Thread(target=open_gripper)
    arm_thread = threading.Thread(target=set_ee_cartesian_trajectory)





    bot.arm.go_to_home_pose()
    #bot.arm.set_ee_cartesian_trajectory(pitch=1.5)
    # Start threads
    gripper_thread.start()
    arm_thread.start()

    # Wait for both threads to complete
    gripper_thread.join()
    arm_thread.join()


    # bot.arm.go_to_home_pose()
    # bot.gripper.open()
    # bot.arm.set_ee_cartesian_trajectory(x=-0.1,y = 0.05,z = -0.2)
   
    
    #bot.arm.set_ee_cartesian_trajectory(z = -0.127)
    bot.gripper.set_pressure(1)

    bot.gripper.close(2.0)
    #bot.gripper.close()
    bot.arm.go_to_sleep_pose()

if __name__=='__main__':
    main()
