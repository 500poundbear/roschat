#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from derek_chat.msg import chat

def talker():
    pub = rospy.Publisher('chatter', chat, queue_size=10)
    rospy.init_node('message_sender', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    msg = chat()
    msg.message.data = "HI"
    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
