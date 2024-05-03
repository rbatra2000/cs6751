# Install script for directory: /home/group8/interbotix_ws/src/interbotix_ros_manipulators/interbotix_ros_xsarms/examples/arm_planning

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/group8/interbotix_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/group8/interbotix_ws/build/interbotix_ros_manipulators/interbotix_ros_xsarms/examples/arm_planning/catkin_generated/installspace/arm_planning.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/arm_planning/cmake" TYPE FILE FILES
    "/home/group8/interbotix_ws/build/interbotix_ros_manipulators/interbotix_ros_xsarms/examples/arm_planning/catkin_generated/installspace/arm_planningConfig.cmake"
    "/home/group8/interbotix_ws/build/interbotix_ros_manipulators/interbotix_ros_xsarms/examples/arm_planning/catkin_generated/installspace/arm_planningConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/arm_planning" TYPE FILE FILES "/home/group8/interbotix_ws/src/interbotix_ros_manipulators/interbotix_ros_xsarms/examples/arm_planning/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/arm_planning" TYPE DIRECTORY FILES "/home/group8/interbotix_ws/src/interbotix_ros_manipulators/interbotix_ros_xsarms/examples/arm_planning/launch")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/arm_planning" TYPE PROGRAM FILES "/home/group8/interbotix_ws/build/interbotix_ros_manipulators/interbotix_ros_xsarms/examples/arm_planning/catkin_generated/installspace/rrt_planning")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/arm_planning" TYPE PROGRAM FILES "/home/group8/interbotix_ws/build/interbotix_ros_manipulators/interbotix_ros_xsarms/examples/arm_planning/catkin_generated/installspace/astar_planning")
endif()

