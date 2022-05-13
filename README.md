# Lab 2: PX manipulation with ROS on python and matlab

Falta:
  -Diagrama del robot.
  -Actualizar en .m las longitudes de los eslabones.
  -Pruebas de todo operativo.

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

---

### Using the MATLAB script









---


First of all, for using both of the scripts you will need to start a ROS master node and launch the turtlesim turtlesim_node. To do that we need two terminal sessions. On the first one run  

`roscore` 

In the second one run: 

`rosrun turtlesim turtlesim_node` 

If everything went well our turtlesim window will pop up with a turtle on it. 

<a href="https://imgbb.com/"><img src="https://i.ibb.co/TLTZQ0Q/Screenshot-from-2022-04-06-20-48-17.png" alt="Screenshot-from-2022-04-06-20-48-17" border="0"></a>

Now launch MATLAB and navigate to the scripts folder of the cloned repository. Once there open the _Lab1.m_ file. It has six sections, the first has three lines where the more relevant is ´rosinit´ because it will allow MATLAB connect to ROS master node. Here you must have the ROS toolbox installed in MATLAB. 

The next section will create a publisher called _velPub_ and a publish message _velMsg_. The third section will assign a value to the message that will be published and that value is a linear type in X direction with a value of 1, then will send the previous configured message to the topic. 

The fourth section generates a subscriber node to get the latest message in the _Pose_ topic. Until here we have already used a publisher and subscriber to use with ROS topics via MATLAB. 

Now, in the fifth section we're going to use the services of this ROS package. You will find a commented line that was an attempt to use the clear service but it wasn't successful. Then you will see the creation of a client related to the _teleport_absolute_ service. After that there's the creation of the message that will be used and the assign of the three values we'll handle, _X_, _Y_ and _angle_, if you run that section the turtle on the turtlesim window will teleport to (3,7) and will be looking towards the upside of the window. 

<a href="https://ibb.co/fMpq6HV"><img src="https://i.ibb.co/PxhFXgs/Screenshot-from-2022-04-06-21-33-01.png" alt="Screenshot-from-2022-04-06-21-33-01" border="0"></a> 

Finally, the ´rosshutdown´ will end MATLAB connection to ROS master node. 

You can close MATLAB as it doesn't have more uses for upcoming parts.

- - -

--- 
## Conclusions
- .

- It was possible to know the main ROS commands, and the importance of its nodes to be connected in both Matlab and Python.

- Be careful when starting the robot's motors, as this can be dangerous.