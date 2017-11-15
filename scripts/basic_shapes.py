#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker

if __name__ == '__main__':
    rospy.init_node('basic_shapes')

    marker_pub = rospy.Publisher('visualization_marker', Marker, None, queue_size = 1)

    shape = Marker.CUBE

    marker = Marker()

    marker.header.frame_id = "/my_frame"
    marker.header.stamp = rospy.Time.now()

    marker.ns = "basic_shapes"
    marker.id = 0

    marker.action = Marker.ADD

    marker.pose.position.x = 0
    marker.pose.position.y = 0
    marker.pose.position.z = 0
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0
       
    marker.scale.x = 1.0
    marker.scale.y = 1.0
    marker.scale.z = 1.0

    marker.color.r = 0.0
    marker.color.g = 1.0
    marker.color.b = 0.0
    marker.color.a = 1.0
        
    marker.lifetime = rospy.Duration()

    while not rospy.is_shutdown():

        marker.type = shape
        
        while marker_pub.get_num_connections() < 1:
            if rospy.is_shutdown():
                exit
            rospy.sleep(1)
            
        marker_pub.publish(marker)
        
        shape += 1
        if shape > Marker.CYLINDER:
            shape = Marker.ARROW

        rospy.sleep(1)
