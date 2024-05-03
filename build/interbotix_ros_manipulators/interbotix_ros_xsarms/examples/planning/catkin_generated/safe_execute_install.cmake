execute_process(COMMAND "/home/group8/interbotix_ws/build/interbotix_ros_manipulators/interbotix_ros_xsarms/examples/planning/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/group8/interbotix_ws/build/interbotix_ros_manipulators/interbotix_ros_xsarms/examples/planning/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
