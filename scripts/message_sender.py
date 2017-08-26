#!/usr/bin/env python

import rospy
import std_msgs
from std_msgs.msg import String
from derek_chat.msg import chat

def talker(user_id):
    pub = rospy.Publisher('chatter', chat, queue_size=10)
    rospy.init_node('message_sender', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        user_message = get_user_message();
        pub.publish(construct_message(user_id, user_message))
        rate.sleep()

def get_user_message():
    print "msg>"
    return raw_input()

def get_user_handle():
    print "What is your handle?"
    return raw_input()

def construct_message_header():
    h = std_msgs.msg.Header()
    h.stamp = rospy.Time.now()
    return h

def construct_message(user_id, message):
    msg = chat()
    msg.header = construct_message_header()
    msg.source_id.data = user_id
    msg.message.data = message
    return msg

if __name__ == '__main__':
    try:
	user_id = get_user_handle()
        talker(user_id)
    except rospy.ROSInterruptException:
        pass
