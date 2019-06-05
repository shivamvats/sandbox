cmake_minimum_required(VERSION 2.8.3)
project(planning)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

find_package(Boost REQUIRED COMPONENTS unit_test_framework)

find_package(Eigen3 REQUIRED)

find_package(catkin
    REQUIRED
    COMPONENTS
        geometry_msgs
        leatherman
        moveit_msgs
        #moveit_ros_planning
        roscpp
        sbpl_collision_checking
        sbpl_kdl_robot_model
        visualization_msgs)

find_package(orocos_kdl REQUIRED)
find_package(OMPL REQUIRED)
find_package(smpl REQUIRED)

catkin_package(
  INCLUDE_DIRS include
#  LIBRARIES planning
#  CATKIN_DEPENDS roscpp
  DEPENDS smpl
)

###########
## Build ##
###########

include_directories(include)
include_directories(SYSTEM ${catkin_INCLUDE_DIRS})
include_directories(SYSTEM ${Boost_INCLUDE_DIRS})
include_directories(SYSTEM ${EIGEN3_INCLUDE_DIR})
include_directories(SYSTEM ${orocos_kdl_INCLUDE_DIRS})

add_executable(callPlanner src/call_planner.cpp src/collision_space_scene.cpp)
target_link_libraries(callPlanner ${catkin_LIBRARIES} smpl::smpl)
target_link_libraries(callPlanner profiler)
