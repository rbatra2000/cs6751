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
    bot = InterbotixManipulatorXS("wx250s", "arm", "gripper", moving_time=3, accel_time=1)
    # bot = InterbotixManipulatorXS("wx250s", "arm", "gripper")
    # bot.dxl.robot_set_operating_modes("group", "arm", "position","time")
    # bot.dxl.robot_set_operating_modes("single", "gripper", "pwm")
    # bot.dxl.robot_set_motor_pid_gains("group", "arm",50,1,0,0,0,1,1)

    bot.dxl.robot_set_motor_pid_gains("group", "arm", kp_pos=300, ki_pos=10)

    # joint_pwms = [10, 10 , 35, 35, 35, 35]
    # bot.dxl.robot_set_motor_pid_gains("group", "arm",4,4,4,4,4,100,1920)
    # bot.dxl.robot_write_commands("arm", joint_pwms)

    # joint_currents = [0, 200 , 200, 50, 0]
    # bot = InterbotixManipulatorXS(robot_model="wx250s")
    # bot.dxl.robot_set_operating_modes("group", "arm", "current")
    # bot.dxl.robot_write_commands("arm", joint_currents)


    if (bot.arm.group_info.num_joints < 5):
        print('This demo requires the robot to have at least 5 joints!')
        sys.exit()


        
    # # Define tasks to be run in parallel
    # def open_gripper():
    #     bot.gripper.open()

    # def set_ee_cartesian_trajectory():
    #     bot.arm.set_ee_cartesian_trajectory(x=-0.1, y=0.05, z=-0.2-0.121, pitch=1.5) #moving_time=None, wp_moving_time=0.85, wp_accel_time=0.5, wp_period=0.05)

    #     sleep(1.0)

    # Create threads
    # gripper_thread = threading.Thread(target=open_gripper)
    # arm_thread = threading.Thread(target=set_ee_cartesian_trajectory)





    bot.arm.go_to_home_pose(blocking = False)
    k = input("Press [ENTER] to continue")

    #bot.arm.set_ee_cartesian_trajectory(pitch=1.5)
    # Start threads
    # gripper_thread.start()
    # arm_thread.start()

    # # Wait for both threads to complete
    # gripper_thread.join()
    # arm_thread.join()

   

    # bot.gripper.set_pressure(1)

    # bot.gripper.close(2.0)
    bot.arm.go_to_sleep_pose(blocking=False)
    k = input("Press [ENTER] to continue")

if __name__=='__main__':
    main()
