I searched the internet for a standard IMU format and found a ROS (robot operating system) package that provides a message type for IMU data.

I made a python script that uses this package and generates random IMU data by varying the variables (such as linear acceleration, angular velocity, and orientation) with sine and cosine functions gently.

The script publishes the IMU data to a ROS topic that can be subscribed by other nodes or applications.
