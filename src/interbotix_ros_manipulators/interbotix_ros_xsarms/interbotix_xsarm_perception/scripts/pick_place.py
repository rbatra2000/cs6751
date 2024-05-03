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
def color_compare(rgb):
    r,g,b = [x/255.0 for x in rgb]
    h,s,v = colorsys.rgb_to_hsv(r,g,b)

    if h < 0.025: color = "red"
    elif 0.025 < h < 0.05: color = "orange"
    elif 0.1 < h < 0.15: color = "yellow"
    elif 0.3 < h < 0.4: color = "green"
    elif 0.55 < h < 0.65: color = "blue"
    elif 0.75 < h < 0.85: color = "purple"
    else: color = "unknown"
    return color

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
    success, clusters = pcl.get_cluster_positions(ref_frame="wx250s/base_link", sort_axis="y", reverse=True)

    # set initial arm and gripper pose
    bot.arm.set_ee_pose_components(x=0.02, z=0.5)
    bot.gripper.open()

    # pick up all the objects and drop them in a virtual basket in front of the robot
    for cluster in clusters:
        x, y, z = cluster["position"]
        print(cluster["position"])
        x = min(x, 0.26)
        bot.arm.set_ee_pose_components(x=x, y=y-0.05, z=z, pitch=0.5)
        bot.arm.set_ee_pose_components(x=x, y=y-0.05, z=z, pitch=0.5)
        bot.gripper.set_pressure(1)
        bot.gripper.close()
        bot.arm.set_ee_pose_components(x=x, y=y-0.05, z=z, pitch=0.5)
        bot.arm.set_ee_pose_components(x=0.02, z=0.5)
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

    bot.arm.set_ee_pose_components(x=0.02, z=0.5)
    bot.arm.go_to_sleep_pose()

if __name__=='__main__':
    main()