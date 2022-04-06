#! /usr/bin/env python

import rospy

from sensor_msgs.msg import LaserScan

def mini(x):
    if (len(x) == 0):
        return (10000,9999)
    else:
        return x

def clbk_laser(msg):
    # 720 / 5 = 144
    regions = [
        min(min(mini(msg.ranges[0:143])), 10),
        min(min(mini(msg.ranges[144:287])), 10),
        min(min(mini(msg.ranges[288:431])), 10),
        min(min(mini(msg.ranges[432:575])), 10),
        min(min(mini(msg.ranges[576:713])), 10),
    ]
    rospy.loginfo(regions)

def main():
    rospy.init_node('reading_laser')
    
    sub = rospy.Subscriber('/my_mm_robot/laser/scan', LaserScan, clbk_laser)
    
    rospy.spin()

if __name__ == '__main__':
    main()
