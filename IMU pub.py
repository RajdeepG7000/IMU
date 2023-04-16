#!/usr/bin/env python
import rospy
import math
from sensor_msgs.msg import Imu
dt = 0.01
t = 0
pub = rospy.Publisher("/imu", Imu, queue_size=10)
    # create a node
rospy.init_node("imu_publisher")

# create a message object
msg = Imu()
while not rospy.is_shutdown():
    
    # fill in the message fields with some dummy data
    msg.header.stamp = rospy.Time.now()
    msg.header.frame_id = "base_link"
    msg.orientation.x = 0.0
    msg.orientation.y = 0.0
    msg.orientation.z = 0.0
    msg.orientation.w = 1.0
    msg.orientation_covariance[0] = -1 # no orientation estimate
    msg.angular_velocity.x = 6 + 2*math.sin(t)# rad/s
    msg.angular_velocity.y = 2 + math.sin(t+((math.pi)/2)) # rad/s
    msg.angular_velocity.z = 7 + math.cos(t) # rad/s
    msg.angular_velocity_covariance[0] = 0.01 # rad/s^2
    msg.linear_acceleration.x = 4.0 + math.sin(t) # m/s^2
    msg.linear_acceleration.y = 3 + math.cos(t) # m/s^2
    msg.linear_acceleration.z = -9.8 # m/s^2
    msg.linear_acceleration_covariance[0] = 0.1 # m/s^4
    
    # publish the message at 10 Hz
    rate = rospy.Rate(10)
    rospy.loginfo("Time = {0}".format(t))
    rospy.loginfo("Linear acceleration along x = {0}".format(msg.linear_acceleration.x))
    rospy.loginfo("Linear acceleration along y = {0}".format(msg.linear_acceleration.y))
    rospy.loginfo("Linear acceleration along z = {0}".format(msg.linear_acceleration.z))
    rospy.loginfo("Angular Velocity about x = {0}".format(msg.angular_velocity.x))
    rospy.loginfo("Angular Velocity about y = {0}".format(msg.angular_velocity.y))
    rospy.loginfo("Angular Velocity about z = {0}".format(msg.angular_velocity.z))
    t = t + dt
    pub.publish(msg)
    rate.sleep()