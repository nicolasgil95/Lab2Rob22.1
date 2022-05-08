%%
clear;
clc;
rosinit; %Conexion nodo maestro
%%
velPub = rospublisher('/turtle1/cmd_vel','geometry_msgs/Twist');%Creacion del publicador
velMsg = rosmessage(velPub); %Creacion del mensaje
%%
velMsg.Linear.X = 1;%Valor del mensaje 
send(velPub,velMsg); %Envio
pause(1);
%%
poseSubs=rossubscriber('/turtle1/pose','turtlesim/Pose'); %Creacion del suscriptor
poseSubs.LatestMessage %ultimo mensaje
%%
%call(clear); %limpiar pantalla 
PoseSvcClient = rossvcclient('/turtle1/teleport_absolute'); %creacion cliente de servicio
PoseMsg = rosmessage(PoseSvcClient);  %Creacion del mensaje 
PoseMsg.X=3 %def pos X
PoseMsg.Y=7 %def pos Y
PoseMsg.Theta = pi/2 %def angulo theta
call(PoseSvcClient,PoseMsg) %llama servicio con el msj definido previamente
%%
rosshutdown