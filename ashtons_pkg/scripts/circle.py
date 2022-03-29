#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def move_circle():

    # Create a publisher which can "talk" to Turtlesim and tell it to move
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    #ASHTON's borrowed code
    rospy.init_node("circle")
    nodename = rospy.get_name()
    rospy.loginfo("- %s node created -" % nodename)
     
    # Create a Twist message and add linear x and angular z values
    move_cmd = Twist()      #From geometry_msgs.msg.
    move_cmd.linear.x = 0.5
    turn_cmd = Twist()
    turn_cmd.angular.z = 1.5

    # Save current time and set publish rate at 10 Hz
    now = rospy.Time.now()
    rate = rospy.Rate(10)

    # For the next 6 seconds publish cmd_vel move commands to Turtlesim
    rospy.loginfo("Beginning circle...")
    while rospy.Time.now() < now + rospy.Duration.from_sec(8):
        pub.publish(turn_cmd)
        rate.sleep()
        pub.publish(move_cmd)
        rate.sleep()

    rospy.loginfo("Circle complete!")

if __name__ == "__main__":
    move_circle()


