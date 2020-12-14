# pygazebo_ros

## Installation

Install `gazebo-ros` package

    sudo apt install ros-melodic-gazebo-ros

Clone de repository and install it.

    git clone https://github.com/qgallouedec/pygazebo_ros
    pip install -e pygazebo_ros

# Usage

```python
import pygazebo_ros

my_gazebo = pygazebo_ros.GazeboROS()
my_gazebo.spawn_light(light_name='my_light', position=[0, 0, 1])