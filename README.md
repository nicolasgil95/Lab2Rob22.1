# Lab 2: PX manipulation with ROS on python and matlab

By: Jhon Brandol Muñoz Romero and Nicolas Gil Rojas

## Abstract
In this lab we try to manipulate the Phantom X robot using the keyboard of our laptop. Also we give a position to the robot using Matlab and get a representation of the current pose using the RVC toolbox.
- - - 
##  Cinematic analysis of the robot
The first one, reference systems are assigned according to the DHstd convention. In this case, you can si the Root Phantom that is plotted with the tool in Matlab. 

<a href="https://imgbb.com/"><img src="https://i.ibb.co/tXtr8yM/pp.jpg" alt="pp" border="0"></a>

Then, there are the convention parameters of DHstd, and it is represented in the following table, where the letter q is variable.Therefore, the measurement is given in centimeters.

 <a href="https://imgbb.com/"><img src="https://i.ibb.co/482tP1q/para.png" alt="para" border="0"></a>

## How to use this repo
Clone this repo onto your Catkin workspace. Also is needed Matlab with dynamixel messages.

With the Phantom X robot connected into your system you have to identify de IDs of the motors and modify them on the _config/joints.yaml_ file. In our case our robot had the ID from 6 to 10.

Compile the package using the following command in a terminal on catkin workspace

`caktin build lab2rob22_1`

Then, source bash 

`source devel/setup.bash`

After this is done and with no errors showed you will be ready to run de scripts.

On the scripts folder there will be a python script named _KeyMove.py_ and 4 matlab scripts: *PX_Robot.m*, _matlabPub.m_, _matlabSub.m_ and _matlabConnectionROSnPX.m_.

# Python Script

The python script can be run using the following commands, on one terminal run:

`roslaunch lab2rob22_1 px_controllers.launch`

on other sourced terminal run:

`rosrun lab2rob22_1 KeyMove.py`

The first command wil enable the communication with the robot, the second one will launch the python script.

After this you should be able to control the robot using you laptop's keyboard:

- Using _W_ and _S_ you will move between joints, it will work cyclical.

- Using _A_ and _D_ the choosen joint will move 90 degrees to left or right.

- Using _R_ the choosen joint will go home.

- Using _H_ the robot will go home.

Also, if you run the next command in other terminal you will visualize the robot in rviz:

`roslaunch lab2rob22_1 px_rviz_dyna.launch`

This is how it'll see on your pc's screen

<a href="https://ibb.co/nDsby4Z"><img src="https://i.ibb.co/jLvTYqB/rvix-Python.png" alt="rvix-Python" border="0"></a>

You will see the video of the robot moving with the keyboard [here](https://youtu.be/rZpshr-DT9Q).

The script is simple: first we import some libraries to python.

<a href="https://imgbb.com/"><img src="https://i.ibb.co/ccmTfWY/LIB.png" alt="LIB" border="0"></a>

Then, there are the definitions of the functions used, one to communicate and send messages to the command service, the second and third ones aren't used as they are the required to connect to the topic and get the current position, but, sadly, we didn't manage to used that current position. Finally, there are two functions to move between joints.

<a href="https://ibb.co/nQc3zSL"><img src="https://i.ibb.co/c2FbDdr/Func.png" alt="Func" border="0"></a>

In the main you'll find the call for the functions. Also there is a part of the code that will give each motor a torque value so the robot won't move very aggresive.

<a href="https://ibb.co/0mD587B"><img src="https://i.ibb.co/JmBZ01x/main.png" alt="main" border="0"></a>

Again, after running this script the terminal will be bugged and won't show any text.

- - -

### Using the MATLAB script

asd
- - -
## Conclusions
- .

- It was possible to know the main ROS commands, and the importance of its nodes to be connected in both Matlab and Python.

- Be careful when starting the robot's motors, as this can be dangerous.