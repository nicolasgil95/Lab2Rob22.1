#!/usr/bin/env python
from operator import le
import rospy
from geometry_msgs.msg import Twist 
from dynamixel_workbench_msgs.srv import DynamixelCommand
import termios, sys, tty
import math

TERMIOS=termios

#Funcion para mover articulacion
def moveart(command, art_ID, addr_name, ang, time):
    rospy.wait_for_service('dynamyxel_workbench/dynamixel_command')
    try:
        value=int((ang+135)/(270/1024)) #conversion de angulos Deg a bits
        dynamixel_command = rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command', DynamixelCommand)
        result = dynamixel_command(command,art_ID,addr_name,value)
        rospy.sleep(time)
        return result.comm_result
    except rospy.ServiceException as exc:
        print(str(exc))

def getkey():
    orig_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin)
    x = 0
    x=sys.stdin.read(1)[0]
    return x

def currentAng(id):
    rospy.init_node('joint_listener', anonymous=True)
    rospy.Subscriber("/dynamixel_workbench/joint_states", jointState, callback)
    rospy.spin()
    
def callback(data):
    rospy.loginfo(data.position)
    

def nextArt():
    if artID==4:
        artID=1
    else:
        artID+=1

def prevArt():
    if artID==1:
        artID=4
    else:
        artID-=1

artID=1
HomeWaist=0
HomeShoulder=90
HomeElbow=0
HomeWrist=0


i=1
if __name__ == '__main__':
    moveart('', 1, 'Torque_Limit', 3*1024/4-1, 0)
    moveart('', 2, 'Torque_Limit', 2*1024/3-1, 0)
    moveart('', 3, 'Torque_Limit', 1024/2-1, 0)
    moveart('', 4, 'Torque_Limit', 1024/3-1, 0)
    while i==1:
        Key=getkey()
        if Key==chr(32): #Tecla H mueve articulaciones a HOME
                moveart('', 1, 'Goal_Position', HomeWaist, 0.5)
                moveart('', 2, 'Goal_Position', HomeShoulder, 0.5)
                moveart('', 3, 'Goal_Position', HomeElbow, 0.5)
                moveart('', 4, 'Goal_Position', HomeWrist, 0.5)
        elif Key==chr(87) or Key==chr(119): #Tecla W mueve entre articulacion
            nextArt()
        elif Key==chr(83) or Key==chr(115): #Tecla S mueve entre articulacion
            prevArt()
        elif Key==chr(65) or Key==chr(97): #Tecla A mueve articulacion a izq
            try:
                moveart('', artID, 'Goal_Position', currentAng(artID)-1, 0.1)
            except rospy.ROSInterruptException:
                pass
        elif Key==chr(68) or Key==chr(100): #Tecla D mueve articulacion a der
            try:
                moveart('', artID, 'Goal_Position', currentAng(artID)+1, 0.1)
            except rospy.ROSInterruptException:
                pass
        elif Key==chr(82) or Key==chr(114): #Tecla R mueve articulacion a home
            if artID==1:
                try:
                    moveart('', 1, 'Goal_Position', HomeWaist, 0)
                except rospy.ROSInterruptException:
                    pass
            elif artID==2:
                try:
                    moveart('', 2, 'Goal_Position', HomeShoulder, 0)
                except rospy.ROSInterruptException:
                    pass
            elif artID==3:
                try:
                    moveart('', 3, 'Goal_Position', HomeElbow, 0)
                except rospy.ROSInterruptException:
                    pass
            elif artID==4:
                try:
                    moveart('', 4, 'Goal_Position', HomeWrist, 0)
                except rospy.ROSInterruptException:
                    pass
        elif Key==chr(27): #ESC
            sys.exit()
