#!/usr/bin/env python

import roslib
import rospy
from geometry_msgs.msg import Twist, TransformStamped
from std_msgs.msg import Empty
import sys
import select
import termios
import tty
import time

speed =  0.2				# default linear speed
turn =   1.0				# default angular speed
pub = rospy.Publisher('/bebop/cmd_vel', Twist, queue_size=1)
pub_takeoff = rospy.Publisher('/bebop/takeoff', Empty, queue_size=10)
pub_land = rospy.Publisher('/bebop/land', Empty, queue_size=10)


print('Take off')
empty = Empty()zs
pub_takeoff.publish(empty)

twist = Twist()



(x,y,z,th) = (0, 0, 1, 0)
twist.linear.x = x * speed
twist.linear.y = y * speed
twist.linear.z = z * speed
twist.angular.x = 0
twist.angular.y = 0
twist.angular.z = th * turn
pub.publish(twist)
time.sleep(2)

(x,y,z,th) = (1, 0, 0, 1)

twist.linear.x = x * speed
twist.linear.y = y * speed
twist.linear.z = z * speed
twist.angular.x = 0
twist.angular.y = 0
twist.angular.z = th * turn
pub.publish(twist)
time.sleep(0.9)

(x,y,z,th) = (1, 0, 0, 0)
twist.linear.x = x * speed
twist.linear.y = y * speed
twist.linear.z = z * speed
twist.angular.x = 0
twist.angular.y = 0
twist.angular.z = th * turn
pub.publish(twist)
time.sleep(0.72)

(x,y,z,th) = (0, 0, -1, 0)

twist.linear.x = x * speed
twist.linear.y = y * speed
twist.linear.z = z * speed
twist.angular.x = 0
twist.angular.y = 0
twist.angular.z = th * turn
pub.publish(twist)
time.sleep(0.95)


print('Landing...')
empty = Empty()
pub_land.publish(empty)





