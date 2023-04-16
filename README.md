My thought process was: 
  1. Generate the data using math library and sin, cos functions to vary the variables gently.
  2. Use a free variable t, and the other variables will be functions of t.
  3. Increment t by very small amount every loop so that the IMU receives gently changing data.
  4. Find a ros package that can help publish IMU data in the standard way.

I searched the internet for a standard IMU format and found a ROS (robot operating system) package that provides a message type for IMU data. 

I copied some code i found online that used that package, and modified it.

I made a python script that uses this package and generates random IMU data by varying the variables (such as linear acceleration, angular velocity, and orientation) with sine and cosine functions gently.

Then integrated the ros aspect into it.

The script publishes the IMU data to a ROS topic that can be subscribed by other nodes or applications.

Attached is the python script, screenshots of both the loginfo and what is being published on the topic (rostopic echo)

This is the link to the rosject: https://app.theconstructsim.com/l/57104f19/
