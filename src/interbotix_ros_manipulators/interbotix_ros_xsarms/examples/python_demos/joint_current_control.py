from interbotix_xs_modules.arm import InterbotixManipulatorXS

# This script commands currents [mA] to the arm joints
#
# To get started, open a terminal and type 'roslaunch interbotix_xsarm_control xsarm_control.launch robot_model:=vx250'
# Then change to this directory and type 'python joint_current_control.py  # python3 bartender.py if using ROS Noetic'

def main():
    joint_currents = [0, 200 , 200, 50, 0]
    bot = InterbotixManipulatorXS(robot_model="wx250s")
    bot.dxl.robot_set_operating_modes("group", "arm", "current")
    bot.dxl.robot_write_commands("arm", joint_currents)

if __name__=='__main__':
    main()
