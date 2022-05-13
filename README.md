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

`roslaunch lab2rob22_1 px_controllers.launch`

on other sourced terminal run:

`rosrun lab2rob22_1 KeyMove.py`

The first command wil enable the communication with the robot, the second one will launch the python script.

After this you should be able to control the robot using you laptop's keyboard:

- Using _W_ and _S_ you will move between articulations, it will work cyclical.

- Using _A_ and _D_ the choosen articulation will move 90 degrees to left or right.

- Using _R_ the choosen articulation will go home.

- Using _H_ the robot will go home.

Also, if you run the next command in other terminal you will visualize the robot in rviz:

`roslaunch lab2rob22_1 px_rviz_dyna.launch`

This is how it'll see on your pc's screen

<a href="https://ibb.co/nDsby4Z"><img src="https://i.ibb.co/jLvTYqB/rvix-Python.png" alt="rvix-Python" border="0"></a>

You will see the video of the robot moving with the keyboard [here](__ENLACE VIDEO TECLADO__).

Again, after running this script the terminal will be bugged and won't show any text.











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
### Python script
To run the python script you must keep the previous executed terminals open and running. On a new terminal run the following command once you're on the catkin workspace directory:  

`source devel/setup.bash` 

This will make this terminal session load the scripts of the packages inside the catkin workspace folder. 

Also, we can call the reset the turtlesim window just to make it look nicer. If you want to, run this commands: 

`rosservice call /reset` 

or, if you like the current turtle model, 

`rosservice call /turtle1/teleport_absolute "x: 5.5 y: 5.5 theta: 0.0" ` 

`rosservice call /clear` 

Now, let's check the script, run a nano command like this from the catkin workspace directory: 

`nano src/Lab1Rob_22.1/scripts/myTeleopKey.py` 

This will open the script in the terminal session. First of all there are the library imports used. Apart from the used in the others python scripts included in the package there's the import of _termios_, _sys_ and _tty_ libraries that will be used to get the pressed key as this [page](https://stackoverflow.com/questions/34497323/what-is-the-easiest-way-to-detect-key-presses-in-python-3-on-a-linux-machine) shows.

Then there's the definition of the functions used for reset, U-turn and movement required. The function teleport uses the service _teleport_absolute_ and will teleport the turtle to the _X_, _Y_ and _ang_ desired inputs, as it's used for resetting the turtle position we're using _5.5_, _5.5_ and _0_  as the input of the function. Therefore, the movement with the R keys to return to its center position and orientation, so the services turtle1/teleport absolute are implemented.

<a href="https://ibb.co/6yFXH6K"><img src="https://i.ibb.co/PrgDcB2/tele.png" alt="tele" border="0"></a>

The next function, _teleport1_ receives two values and uses the _teleport_relative_ service. As the function is used to the U-turn of the turtle the input will be _0_ and _math.pi_. Then is defined the function pubVel which is used to do the movements of the turtle being a publisher for the topic _/turtle1/cmd_vel_. As we don't need a _Y_ axis movement we only need two inputs, one for the linear move and the other one for angular rotation.  

<a href="https://ibb.co/GFYn4dt"><img src="https://i.ibb.co/1by7t0d/tele1.png" alt="tele1" border="0"></a>

Finally there's defined the function to read the keys. Then appears the main routine that will check which key is pressed and only reacts to: _W_, _S_, _A_ and _D_ for movement and rotations, _space_ for U-turn, and _R_ to reset turtle position and _Esc_ to end the python process.  

Now that you know how that code works you can get out of nano editor using _ctrl+x_ and run the scrip using the command 

`rosrun hello_turtle myTeleopKey.py` 

<a href="https://ibb.co/Z883Tnp"><img src="https://i.ibb.co/wWWT69F/ejem1.png" alt="ejem1" border="0"></a>

It can be seen that the turtle moved forward because the letter w on the keyboard was pressed. Then, the letter R is pressed, which has ubicated the turtle where it was initially.

<a href="https://imgbb.com/"><img src="https://i.ibb.co/z64dJjQ/ejempl2.png" alt="ejempl2" border="0"></a>

Check the turtlesim window as you press the previously mentioned keys to see the movement. Once you saw the turtle moving can close using _Esc_. 

__There's a bug using this file that, after closing the interaction, the terminal session where the file was executed will no show the text write onto it but it'll be recorded anyway.__ 

--- 
## Conclusions
-After doing the scripts we have understood how to connect MATLAB to ROS master node and the to use the topics and services. Also we can start creating scripts for ROS packages in Python and use the services and topics.

-It was possible to know the main ROS commands, and the importance of its nodes to be connected in both Matlab and Python.

