#!/usr/bin/env python
from operator import le
import rospy
from geometry_msgs.msg import Twist 
from turtlesim.srv import TeleportAbsolute, TeleportRelative
import termios, sys, tty
import math

TERMIOS=termios

def teleport(x, y, ang):
    rospy.wait_for_service('/turtle1/teleport_absolute')
    try:
        teleportA = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute) 
        resp1 = teleportA(x, y, ang)
        print('Teleported to x: {}, y: {}, ang: {}'.format(str(x),str(y),str(ang)))
    except rospy.ServiceException as e:
        print(str(e))
def teleport1(li,ang):
    rospy.wait_for_service('/turtle1/teleport_relative')
    try:
        teleportB = rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative) 
        resp2 = teleportB(li,ang)
        #print('Teleported to x: {}, y: {}, ang: {}'.format(str(x),str(y),str(ang)))
    except rospy.ServiceException as e:
        print(str(e))

def pubVel(xvel, zvel):
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('velPub', anonymous=False)
    vel = Twist()
    rate = rospy.Rate(10) 
    vel.linear.x = xvel
    vel.angular.z = zvel
    rospy.loginfo(vel)
    pub.publish(vel)
    rate.sleep()

def getkey():
    orig_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin)
    x = 0
    x=sys.stdin.read(1)[0]
    return x

i=1
if __name__ == '__main__':
    while i==1:
        Key=getkey()
        if Key==chr(32): #espacio=char   
                teleport1(0,  math.pi)
        elif Key==chr(87) or Key==chr(119): #W 
            try:
                pubVel(1,0)
            except rospy.ROSInterruptException:
                pass
        elif Key==chr(83) or Key==chr(115): #S
            try:
                pubVel(-1,0)
            except rospy.ROSInterruptException:
                pass
        elif Key==chr(65) or Key==chr(97): #A
            try:
                pubVel(0,1)
            except rospy.ROSInterruptException:
                pass
        elif Key==chr(68) or Key==chr(100): #D
            try:
                pubVel(0,-1)
            except rospy.ROSInterruptException:
                pass
        elif Key==chr(82) or Key==chr(114): #R
            try:
                teleport(5.5, 5.5, 0)
            except rospy.ROSInterruptException:
                pass
        elif Key==chr(27): #ESC
            sys.exit()
