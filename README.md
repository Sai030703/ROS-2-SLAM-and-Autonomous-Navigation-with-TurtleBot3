# ROS-2-SLAM-and-Autonomous-Navigation-with-TurtleBot3

# Overview

This project demonstrates autonomous navigation in a simulated environment using ROS 2 and TurtleBot3. It integrates SLAM Toolbox for mapping, Nav2 Stack for navigation, and Rviz2 for real-time visualization and interaction.


# Features

* 2D Mapping: Created a 2D map using the Cartographer node from the SLAM Toolbox.
* Autonomous Navigation: Executed single-point and multi-pose navigation tasks.
* Visualization: Monitored and interacted with the robot via Rviz2.
* Simulation: Entirely simulated in the Gazebo environment using the TurtleBot3 robot model 

# Getting Started
Prerequisites
ROS 2 (Rolling/Humble/Foxy) installed on your system.
TurtleBot3 Simulation Packages

    
    sudo apt install ros-<ros2-distro>-turtlebot3*  

Gazebo ROS Packages.
    
    sudo apt install ros-<distro-name>-gazebo-ros-pkgs

 SLAM Toolbox

    sudo apt install ros-<distro-name>-slam-toolbox
    
    
Gazebo Simulator and necessary dependencies installed.

# Installation
Clone this repository:

    git clone https://github.com/Sai030703/ROS-2-SLAM-and-Autonomous-Navigation-with-TurtleBot3.git   
    
Install dependencies (if any):

    rosdep install --from-paths src --ignore-src -r -y  
    
    Build the workspace: cd <your_ros2_ws>
    colcon build
    source install/setup.bash  
    
 
# How to Run

To launch the navigation stack, use the following command:

    ros2 launch navigation navigation.launch.py

