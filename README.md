# Lab 2: PX manipulation with ROS on python and matlab

Falta:
  -Diagrama del robot.
  -Actualizar en .m las longitudes de los eslabones.
  -Pruebas de todo operativo.

By: Jhon Brandol Muñoz Romero and Nicolas Gil Rojas
## Abstract
In this lab we try to manipulate the Phantom X robot using the keyboard of our laptop. Also we give a position to the robot using Matlab and get a representation of the current pose using the RVC toolbox.
 - - - 
## How to use this repo
Clone this repo onto your Catkin workspace. Also is needed Matlab with dynamixel messages.

Compile the package using the following command in a terminal on catkin workspace

`caktin build lab2rob22_1`

Then, source bash 

`source devel/setup.bash`

After this is done and with no errors showed you will be ready to run de scripts.

On the scripts folder there will be a python script named _KeyMove.py_ and 4 matlab scripts: *PX_Robot.m*, _matlabPub.m_, _matlabSub.m_ and _matlabConnectionROSnPX.m_.

# Python Script

The python script can be run using the following commands, on one terminal run:

`roscore`

on other sourced terminal run:

`rosrun lab2rob22_1 KeyMove.py`

After this you should be able to control the robot using you laptop's keyboard:

- Using _W_ and _S_ you will move between articulations, it will work cyclical.

- Using _A_ and _D_ the choosen articulation will move to left or right.

- Using _R_ the choosen articulation will go home.

- Using _H_ the robot will go home.



After having installed the software mentioned there go to your catkin workspace and on the src folder clone this repo, you can follow the next commands in terminal: 

`cd catkin_ws/src` 

`git clone https://github.com/nicolasgil95/Lab1Rob_22.1`

Once cloned has finished, go back to Catkin workspace directory and build the package. This can be done with the following commands: 

`cd ..` 

`caktin build hello_turtle` 

In case you haven't installed Catkin tools you can run `catkin_make` to build the package.

__Be sure you don't have any other package with the name hello_turtle in the Catkin source folder because it will show an error when compiling__


Anyway, after that's done you're ready to check and run the new scripts. 
- - -
### Using the MATLAB script


This is the link to watch the video:

- - -
### Python script


__There's a bug using this file that, after closing the interaction, the terminal session where the file was executed will no show the text write onto it but it'll be recorded anyway.__ 

--- 
## Conclusions
-After doing the scripts we have understood how to connect MATLAB to ROS master node and the to use the topics and services. Also we can start creating scripts for ROS packages in Python and use the services and topics.

-It was possible to know the main ROS commands, and the importance of its nodes to be connected in both Matlab and Python.

