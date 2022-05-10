clear; clc;
rosinit;

jointSub=rossubscriber('/joint_states','sensor_msgs/JointState'); %Creacion del suscriptor
jointSub.LatestMessage


rosshutdown;