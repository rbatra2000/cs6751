import time
import colorsys
from interbotix_xs_modules.arm import InterbotixManipulatorXS
from interbotix_perception_modules.apriltag import InterbotixAprilTagInterface
from interbotix_perception_modules.pointcloud import InterbotixPointCloudInterface
# from interbotix_ros_toolboxes.interbotix_perception_toolbox.interbotix_perception_modules.setup import PictureSnapper

# interbotix_ros_toolboxes/interbotix_perception_toolbox/interbotix_perception_modules/scripts/picture_snapper
# from interbotix_ros_toolboxes.interbotix_perception_toolbox.interbotix_perception_modules.scripts import PictureSnapper

from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np

#!/usr/bin/env python
import os
import rospy
import threading
from sensor_msgs.msg import Image
from interbotix_perception_modules.srv import SnapPicture, SnapPictureResponse


# To start this application, open a terminal on the robot and type...
#   'roslaunch interbotix_perception_modules picture_snapper.launch'
#
# To save a picture, open a new terminal in this directory and type...
#   'rosservice call /apriltag/snap_picture "filename: '[filename].jpg'"'

### @brief Class to get the latest picture from the camera and save it to a file with a specified name
### @details - meant to run on the same computer with the AprilTag Single Image Server node;
###            this way, all images will be saved to the same computer so that the AprilTag
###            Single Image Server node can access them
# class PictureSnapper(object):
#     def __init__(self):
#         self.image = None
#         self.img_mutex = threading.Lock()

#         # topic containing raw rgb data
#         # self.camera_color_topic = rospy.get_param("camera_color_topic").strip("/")
#         # self.sub_camera_color = rospy.Subscriber("/" + self.camera_color_topic, Image, self.camera_color_cb)

#         # apriltag_ns = rospy.get_param("~apriltag_ns", default="apriltag")

#         # # directory in which to save pictures (leave this as is)
#         # dir_param = rospy.get_param(
#         #     "/" + apriltag_ns + "/picture_snapper/image_save_dir", 
#         #     default="interbotix/picture_snapper/")
#         # self.image_save_dir = os.path.dirname(dir_param)
#         self.full_image_save_dir = "/home/group8/interbotix_ws/src/interbotix_ros_manipulators/interbotix_ros_xsarms/interbotix_xsarm_perception/scripts/assets"

#         try: # check if directory exists, if not make one
#             # if not os.path.exists(self.image_save_dir):
#             #     os.makedirs(self.image_save_dir)
#             rospy.loginfo("Saving images to: " + self.full_image_save_dir)
#         except Exception as e: # if we fail (permissions, etc.)
#             rospy.logerr("Failed to create directory: " + e)
#             exit()

#         # rospy.loginfo("Ready to save image from topic: " + self.camera_color_topic)
#         # rospy.Service('snap_picture', SnapPicture, self.snap_picture)
#         # while (self.image == None and not rospy.is_shutdown()): pass

#     ### @brief ROS Subscriber Callback to get the latest color image
#     ### @param msg - ROS Image message
#     def camera_color_cb(self, msg):
#         with self.img_mutex:
#             self.image = msg

#     ### @brief ROS Service Callback to save the latest rgb picture with the desired name
#     ### @param req - ROS 'SnapPicture' Service message
#     def snap_picture(self, req):
#         res = SnapPictureResponse()
#         res.success = False
#         res.filepath = "NULL"
#         bridge = CvBridge()
#         with self.img_mutex:
#             try:
#                 cv_image = bridge.imgmsg_to_cv2(self.image, "bgr8")
#                 cv2.imwrite(os.path.join(self.image_save_dir, req.filename), cv_image)
#                 filepath = os.path.join(self.full_image_save_dir, req.filename)
#                 rospy.loginfo("Image saved to " + filepath)
#                 res.success = True
#                 res.filepath = filepath
#             except Exception as e:
#                 rospy.logerr("Failed to save image.")
#                 rospy.logerr(e)
#         return res

# def main():
#     rospy.init_node('picture_snapper')
#     PictureSnapper()
#     rospy.spin()

# if __name__=='__main__':
#     main()



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

bridge = CvBridge()

def show_image(img):
     cv2.imshow("Window", img)
     cv2.waitKey(3)


def image_callback(img_msg):
        # rospy.loginfo(img_msg.header)

        try:
            image = bridge.imgmsg_to_cv2(img_msg, "passthrough")
            # show_image(cv_image)

            frame = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
            res = frame.copy()
    
            # lower_blue = np.array([100,150,0])
            # upper_blue = np.array([140,255,255])
            lower_blue = np.array([10,100,20])
            upper_blue = np.array([25,255,255])

            lower_green = np.array([25,50,50])
            upper_green = np.array([100,255,255])

            mask = cv2.inRange(frame, lower_green, upper_green)

            print(cv2.countNonZero(mask))

            # okay now lets create contours so we can identify the blue objects
            bluecnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

            if len(bluecnts) > 0:
                 for cnt in bluecnts:
                    #   area =cv2.contourArea(cnt)
                    #   print(area)
                    (xg,yg,wg,hg) = cv2.boundingRect(cnt)
                    cv2.rectangle(image,(xg,yg), (xg+wg, yg+hg), (0,255,0), 2)

                    cv2.circle(image, ((int)(xg+wg/2), (int)(yg+hg/2)), 2, (0, 255, 0), 2)



            res = cv2.bitwise_and(res, res, mask=mask)
            cv2.imshow('raw', image)
            cv2.imshow('frame', frame)
            cv2.imshow('mask', mask)
            cv2.imshow('res', res)
            

            # get locations
            # _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            # contours = [cv2.boundingRect(cnt) for cnt in contours]
            # for cnt in contours:
            #     x,y,w,h = cnt
            #     print(x,y)
            # print("")
            # locations = cv2.findNonZero(mask)
            # print(len(locations))

            k = cv2.waitKey(5) & 0xFF
        except CvBridgeError as e:
             rospy.logerr("CvBridge Error: {0}".format(e))
        


def main():
    # Initialize the arm module along with the pointcloud and armtag modules
    bot = InterbotixManipulatorXS("wx250s", moving_time=3, accel_time=0.75)
    pcl = InterbotixPointCloudInterface()

    # camera_info_topic = rospy.get_param(
    #         "/" + "apriltag" + "/camera_info_topic",
    #         default="camera/color/image_raw").strip("/")
    # print(camera_info_topic)
    sub_image = rospy.Subscriber("/camera/color/image_raw", Image, image_callback)
    # TEST
    # cv2.namedWindow("Window", 1)

    # while not rospy.is_shutdown():
    rospy.spin()
    # apriltag = InterbotixAprilTagInterface()
    # picture_snapper = PictureSnapper()
    # picture_snapper = PictureSnapper()

    # bridge = CvBridge()

    # image = bridge.imgmsg_to_cv2(apriltag._snap()..)
    # image = apriltag._snap()

    # print(image)
    # bridge = CvBridge()
    # cv_image = bridge.imgmsg_to_cv2(image, desired_encoding="passthrough")
    # print(cv_image)
    # except Exception as e:
    # rospy.logerr("Failed to save image.")
    # rospy.logerr(e)

    

    # # get the ArmTag pose
    # # bot.arm.set_ee_pose_components(x=0.02, z=0.4)
    # # time.sleep(0.5)
    # # bot.arm.set_ee_pose_components(y=-0.1, z=0.2)

    # # time.sleep(0.5)
    # # armtag.find_ref_to_arm_base_transform()
    # # bot.arm.set_ee_pose_components(x=0, z=0)

    # # get the cluster positions
    # # sort them from max to min 'x' position w.r.t. the 'wx200/base_link' frame
    # success, clusters = pcl.get_cluster_positions(ref_frame="wx250s/base_link", sort_axis="y", reverse=True)

    # # set initial arm and gripper pose
    # bot.arm.set_ee_pose_components(x=0.02, z=0.5)
    # bot.gripper.open()

    # # pick up all the objects and drop them in a virtual basket in front of the robot
    # for cluster in clusters:
    #     x, y, z = cluster["position"]
    #     print(cluster["position"])
    #     x = min(x, 0.26)
    #     bot.arm.set_ee_pose_components(x=x, y=y-0.05, z=z, pitch=0.5)
    #     bot.arm.set_ee_pose_components(x=x, y=y-0.05, z=z, pitch=0.5)
    #     bot.gripper.set_pressure(1)
    #     bot.gripper.close()
    #     bot.arm.set_ee_pose_components(x=x, y=y-0.05, z=z, pitch=0.5)
    #     bot.arm.set_ee_pose_components(x=0.02, z=0.5)
    #     bot.gripper.open()



    #     # clr = color_compare(cluster["color"])
    #     # print(clr)
    #     # if (clr == "yellow"):
    #     #     bot.arm.set_ee_pose_components(x=0.2, y=-0.24, z=.2)
    #     # elif (clr == "orange"):
    #     #     bot.arm.set_ee_pose_components(x=0.2, y=-0.1, z=.2)
    #     # else:
    #     #     # if color cannot be recognized, then put the block back...
    #     #     bot.arm.set_ee_pose_components(x=x, y=y, z=z+0.08, pitch=0.5)
    #     # bot.gripper.open()
    #     # bot.arm.set_ee_pose_components(x=0.3, z=0.2)

    # bot.arm.set_ee_pose_components(x=0.02, z=0.5)
    # bot.arm.go_to_sleep_pose()

if __name__=='__main__':
    main()