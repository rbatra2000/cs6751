import numpy as np
import math
import rospy
import time
import cv2
from threading import Lock
import message_filters
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image, CameraInfo
from visualization_msgs.msg import Marker, MarkerArray
from scipy.spatial.transform import Rotation
from geometry_msgs.msg import Pose
from interbotix_common_modules.utils import TFUtils

# ASSUMPTIONS: minimum grape and leaf area
MIN_GRAPE_AREA = 50
MIN_LEAF_AREA = 50
MAX_LEAF_AREA = 500

class Grape:
    def __init__(self, name, loc, bias):
        self.name = name
        self.loc = loc
        self.bias = bias

class PixelSelector:
    def __init__(self):
        pass

    def load_image(self, img):
        self.img = img

    # if the leaf is intersection with the grape, we can determine the occlusion
    def intersection(self,a,b):
        if a[0]+a[2] < b[0] or a[0] > b[0]+b[2] or a[1]+a[3] < b[1] or a[1]>b[1]+b[3]:
            return False
        return True

    # get the coordinates of the grapes
    def get_grape_coordinates(self):
        # get locations of grapes (Grape Objects)
        grapes = []

        frame = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

        # ASSUMPTIONS: Using blue color range instead of red for the grapes due to HSV color space
        lower_red = np.array([90,50,0])
        upper_red = np.array([150,255,255])

        # create a mask for the red color
        mask = cv2.inRange(frame, lower_red, upper_red)

        # get contours of the red color
        redCnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

        # counter of number of grape number
        grapeNum = 0

        if len(redCnts) > 0:
            for cnt in redCnts:
                area =cv2.contourArea(cnt)

                # we are adding a threshold to make sure that we have valid grapes
                if area < MIN_GRAPE_AREA:
                    print("Skipped grape due to small area")
                    continue

                (xg,yg,wg,hg) = cv2.boundingRect(cnt)
                center_x, center_y= ((int)(xg+wg/2), (int)(yg+hg/2))

                # here are green ranges
                lower_green = np.array([25,50,50])
                upper_green = np.array([90,255,255])

                # create green mask this time
                green_mask = cv2.inRange(frame.copy(), lower_green, upper_green)

                # get contours to separate the leaves
                greencnts = cv2.findContours(green_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

                bias = 0
                # see if the bounding box of any leaves are overlapping with the grape
                for gCnt in greencnts:
                    (xl, yl, wl, hl) = cv2.boundingRect(gCnt)
                    area =cv2.contourArea(gCnt)

                    # we are adding a threshold to make sure that we have valid grapes
                    if area < MIN_LEAF_AREA or area > MAX_LEAF_AREA:
                        continue

                    if self.intersection((xl,yl,wl,hl), (xg,yg,wg,hg)):
                        cv2.rectangle(self.img,(xl,yl), (xl+wl, yl+hl), (0,255,0), 2)
                        leaf_x, _ = ((int)(xl+wl/2), (int)(yl+hl/2))
                        if leaf_x < center_x:
                            bias = 1 # if leaf is on left
                        else:
                            bias = 2 # if leaf is on right
                        break

                grapeName = 'Grape' + str(grapeNum)
                grape = Grape(grapeName, (center_x, center_y), bias)
                print("GRAPE", grapeName, "at", grape.loc, "with bias", grape.bias)
                grapes.append(grape)
                grapeNum += 1

        grapes = sorted(grapes, key=lambda g: g.loc[0], reverse=True)

        return grapes

    def run(self, img):
        self.load_image(img)
        return self.get_grape_coordinates()
    
# Class to interface with RealSense camera (made by rajat)
class RealSenseROS:

    def __init__(self):
        self.bridge = CvBridge()

        self.camera_lock = Lock()
        self.camera_header = None
        self.camera_color_data = None
        self.camera_info_data = None
        self.camera_depth_data = None

        queue_size = 1000

        self.color_image_sub = message_filters.Subscriber("/camera/color/image_raw", Image, queue_size= queue_size, buff_size = 65536*queue_size)
        self.camera_info_sub = message_filters.Subscriber("/camera/color/camera_info", CameraInfo, queue_size= queue_size, buff_size = 65536*queue_size)
        self.depth_image_sub = message_filters.Subscriber("/camera/aligned_depth_to_color/image_raw", Image, queue_size= queue_size, buff_size = 65536*queue_size)
        ts_top = message_filters.TimeSynchronizer([self.color_image_sub, self.camera_info_sub, self.depth_image_sub], queue_size= queue_size)
        ts_top.registerCallback(self.rgbdCallback)
        ts_top.enable_reset = True

        self.point_visualization_pub = rospy.Publisher('point_visualization_marker_array', MarkerArray, queue_size=10)

        time.sleep(1.0)

    def rgbdCallback(self, rgb_image_msg, camera_info_msg, depth_image_msg):
        try:
            # Convert your ROS Image message to OpenCV2
            rgb_image = self.bridge.imgmsg_to_cv2(rgb_image_msg, "passthrough")
            depth_image = self.bridge.imgmsg_to_cv2(depth_image_msg, "32FC1")
        except CvBridgeError as e:
            print(e)

        with self.camera_lock:
            self.camera_header = rgb_image_msg.header
            self.camera_color_data = rgb_image
            self.camera_info_data = camera_info_msg
            self.camera_depth_data = depth_image

    def get_camera_data(self):
        with self.camera_lock:
            return self.camera_header, self.camera_color_data, self.camera_info_data, self.camera_depth_data
    
    def pixel2World(self, camera_info, image_x, image_y, depth_image, box_width = 2):

        if image_y >= depth_image.shape[0] or image_x >= depth_image.shape[1]:
            return False, None

        depth = depth_image[image_y, image_x]

        if math.isnan(depth) or depth < 50 or depth > 2000:

            depth = []
            for i in range(-box_width,box_width):
                for j in range(-box_width,box_width):
                    if image_y+i >= depth_image.shape[0] or image_x+j >= depth_image.shape[1]:
                        return False, None
                    pixel_depth = depth_image[image_y+i, image_x+j]
                    if not (math.isnan(pixel_depth) or pixel_depth < 50 or pixel_depth > 2000):
                        depth += [pixel_depth]

            if len(depth) == 0:
                return False, None

            depth = np.mean(np.array(depth))

        depth = depth/1000.0 # Convert from mm to m

        fx = camera_info.K[0]
        fy = camera_info.K[4]
        cx = camera_info.K[2]
        cy = camera_info.K[5]  

        # Convert to world space
        world_x = (depth / fx) * (image_x - cx)
        world_y = (depth / fy) * (image_y - cy)
        world_z = depth

        return True, np.array([world_x, world_y, world_z])

    def world2Pixel(camera_info, world_x, world_y, world_z):

        fx = camera_info.K[0]
        fy = camera_info.K[4]
        cx = camera_info.K[2]
        cy = camera_info.K[5]  

        image_x = world_x * (fx / world_z) + cx
        image_y = world_y * (fy / world_z) + cy

        return image_x, image_y
    
    def get_pose_msg_from_transform(self, transform):

        pose = Pose()
        pose.position.x = transform[0,3]
        pose.position.y = transform[1,3]
        pose.position.z = transform[2,3]

        quat = Rotation.from_matrix(transform[:3,:3]).as_quat()
        pose.orientation.x = quat[0]
        pose.orientation.y = quat[1]
        pose.orientation.z = quat[2]
        pose.orientation.w = quat[3]

        return pose
    
    def visualize_point(self, transform, id = 0):

        # publish a cube marker
        marker_array = MarkerArray()
        marker = Marker()
        marker.id = id
        marker.header.stamp = rospy.Time.now()
        marker.header.frame_id = "camera_color_optical_frame"
        marker.type = marker.CUBE
        marker.action = marker.ADD
        marker.scale.x = 0.05
        marker.scale.y = 0.05
        marker.scale.z = 0.05
        marker.color.a = 1.0

        # marker color is red
        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 0.0

        pose = self.get_pose_msg_from_transform(transform)
        marker.pose = pose

        marker_array.markers.append(marker)

        self.point_visualization_pub.publish(marker_array)

    def get_grapes_world_coordinates(self):
        _, color_data, info_data, depth_data = self.get_camera_data()   
        pixel_selector = PixelSelector()
        utils = TFUtils()
        pixel_selector.load_image(color_data)
        grapes = pixel_selector.get_grape_coordinates()

        # TODO: Can sort the grape2D if have time

        for grape in grapes:
            valid, world_coordinate = self.pixel2World(info_data, grape.loc[0], grape.loc[1], depth_data)
            
            if valid:
                point_transform = np.eye(4)
                point_transform[:3,3] = world_coordinate.reshape(1,3)
            
                self.visualize_point(point_transform)
                world_coordinate = list(world_coordinate)

                # publish the grape location to the tf
                utils.publishTransformationToTF("camera_color_optical_frame", grape.name, point_transform)

            else:
                rospy.loginfo("Pixel selected has invalid depth :(")
        return grapes
