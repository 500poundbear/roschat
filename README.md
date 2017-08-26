### Derek Chat

A simple chat application to demonstrate ROS topic functionality, as part of the W1 assignment issued by Bumblebee.

#### Parts of the system

message_viewer is the window that receives all the messages sent to the topic.

message_sender is the prompt for users to enter their messages that will be broadcasted across the topic for others to pick up.

#### How to run

Execute the following commands in separate windows:

- roscore
- rosrun derek_chat message_viewer.py
- rosrun derek_chat message_sender.py

Enjoy!
