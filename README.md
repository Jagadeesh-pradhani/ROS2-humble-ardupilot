# ROS2-humble-ardupilot

## Requirements

1. UBUNTU 22.04 LTS
2. ROS-Humble
3. Gazebo-garden
4. Ardupilot

## UBUNTU 22.04 LTS

1. Install and setup in Virtual box or dual boot.
https://ubuntu.com/download/desktop

## ROS-Humble

1. Referred from https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html

2. Steps to install and setup
   1. Set locale
     ```
     locale
     sudo apt update && sudo apt install locales
     sudo locale-gen en_US en_US.UTF-8
     sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
     export LANG=en_US.UTF-8
     ```
   2. Setup Sources
      ```
      sudo apt install software-properties-common
      sudo add-apt-repository universe
      sudo apt update && sudo apt install curl -y
      sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
      ```
      ```
      echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
      ```
   3. Install ROS
      ```
      sudo apt update
      sudo apt upgrade
      sudo apt install ros-humble-desktop-full
      ```
   4. Environment setup
      ```
      source /opt/ros/humble/setup.bash
      echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
      ```
3. Test by running ```ros2```
   output will be
   ```
   usage: ros2 [-h] [--use-python-default-buffering]
            Call `ros2 <command> -h` for more detailed usage. ...
    ros2 is an extensible command-line tool for ROS 2.
    options:
      -h, --help            show this help message and exit
      --use-python-default-buffering
                        Do not force line buffering in stdout and instead use
                        the python default buffering, which might be affected
                        by PYTHONUNBUFFERED/-u and depends on whatever stdout
                        is interactive or not
    Commands:
      action     Various action related sub-command
      bag        Various rosbag related sub-commands    
      component  Various component related sub-commands    
      daemon     Various daemon related sub-commands    
      doctor     Check ROS setup and other potential issues    
      interface  Show information about ROS interfaces    
      launch     Run a launch file    
      lifecycle  Various lifecycle related sub-commands    
      multicast  Various multicast related sub-commands    
      node       Various node related sub-commands    
      param      Various param related sub-commands    
      pkg        Various package related sub-commands    
      run        Run a package specific executable    
      security   Various security related sub-commands    
      service    Various service related sub-commands    
      topic      Various topic related sub-commands    
      wtf        Use `wtf` as alias to `doctor`        
      Call `ros2 <command> -h` for more detailed usage.
   ```

## Gazebo - garden

1. Referred from <br>
   https://gazebosim.org/docs/garden/install_ubuntu
   https://gazebosim.org/docs/garden/ros_installation
