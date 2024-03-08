import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node


def generate_launch_description():

    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')),
        launch_arguments={
            'gz_args': '-r iris_runway.sdf'
        }.items(),
    )

    # RQt
    rqt = Node(
        package='rqt_image_view',
        executable='rqt_image_view',
        arguments=[LaunchConfiguration('image_topic')],
        condition=IfCondition(LaunchConfiguration('rqt'))
    )

    # Bridge
    bridge = Node(
        package='ros_gz_image',
        executable='image_bridge',
        arguments=['camera', 'depth_camera', 'rgbd_camera/image', 'rgbd_camera/depth_image'],
        output='screen'
    )

    bridge1 = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/gimbal/cmd_roll@std_msgs/msg/Float64@gz.msgs.Double',
                   '/gimbal/cmd_tilt@std_msgs/msg/Float64@gz.msgs.Double',
                   '/gui/camera/pose@geometry_msgs/msg/Pose@gz.msgs.Pose',
                   '/world/iris_runway/model/iris_with_gimbal/joint_state@sensor_msgs/msg/JointState@gz.msgs.Model',
                   '/world/iris_runway/dynamic_pose/info@geometry_msgs/msg/PoseArray@gz.msgs.Pose_V'],
        output='screen'
    )
    

    return LaunchDescription([
        gz_sim,
        DeclareLaunchArgument('rqt', default_value='true',
                              description='Open RQt.'),
        DeclareLaunchArgument('image_topic', default_value='/camera',
                              description='Topic to start viewing in RQt.'),
        bridge,
        bridge1,
        rqt
    ])
