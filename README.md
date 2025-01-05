# ROS-2-SLAM-and-Autonomous-Navigation-with-TurtleBot3

# Overview

This project demonstrates autonomous navigation in a simulated environment using ROS 2 and TurtleBot3. It integrates SLAM Toolbox for mapping, Nav2 Stack for navigation, and Rviz2 for real-time visualization and interaction.

# Features

* 2D Mapping: Created a 2D map using the Cartographer node from the SLAM Toolbox.
* Autonomous Navigation: Executed single-point and multi-pose navigation tasks.
* Visualization: Monitored and interacted with the robot via Rviz2.
* Simulation: Entirely simulated in the Gazebo environment using the TurtleBot3 robot model.


# Getting Started
Prerequisites
    ROS 2 (Rolling/Humble/Foxy) installed on your system.
    TurtleBot3 Simulation Packages

    
    sudo apt install ros-<ros2-distro>-turtlebot3*  
    
Gazebo Simulator and necessary dependencies installed.

# Installation
Clone this repository:
    git clone <your-repo-link>  
    cd <repo-name>  
Install dependencies (if any):
    rosdep install --from-paths src --ignore-src -r -y  
    Build the workspace:
    colcon build  
    source install/setup.bash  
 
# How to Run
Step 1: Launch the Simulation
Launch the TurtleBot3 in Gazebo:
    ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py  
Step 2: Create a Map
Run the SLAM Toolbox to generate a 2D map:

bash
Copy code
ros2 launch turtlebot3_cartographer cartographer.launch.py  
Save the map:

bash
Copy code
ros2 run nav2_map_server map_saver_cli -f ~/map  
Step 3: Launch Navigation
Run the Nav2 stack for navigation:

bash
Copy code
ros2 launch nav2_bringup navigation_launch.py map:=~/map.yaml  
Step 4: Visualize and Navigate
Open Rviz2 to monitor the robot’s progress:
bash
Copy code
ros2 launch nav2_bringup rviz_launch.py  
Set single or multiple navigation goals in Rviz2.

