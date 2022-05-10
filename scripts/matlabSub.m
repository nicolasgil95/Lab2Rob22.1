clear; clc;
rosinit;

jointSub=rossubscriber('/joint_states','dynamixel_workbench_msgs/DynamixelStateList'); %Creacion del suscriptor
jointSub.LatestMessage

rosshutdown;