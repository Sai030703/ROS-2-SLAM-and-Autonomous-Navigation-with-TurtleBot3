import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    # Define paths to configuration files
    config_dir = os.path.join(get_package_share_directory('navigation'), 'config')
    map_file = os.path.join(config_dir, 'tb3_map.yaml')
    param_file = os.path.join(config_dir, 'house_nav_params.yaml')
    rviz_config_dir = os.path.join(config_dir, 'navigation.rviz')

    #turtlebot3_dqn_stage4.launch.py
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([get_package_share_directory('turtlebot3_gazebo'),'/launch','/turtlebot3_dqn_stage4.launch.py'])
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([get_package_share_directory('nav2_bringup'),'/launch','/bringup_launch.py']),
            launch_arguments={
            'map':map_file,
            'params_file': param_file}.items(),

        ),


    Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2_node',
        arguments=['-d', rviz_config_dir],
        output='screen'

        ),
    ])


