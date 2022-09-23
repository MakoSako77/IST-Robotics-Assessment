#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()
LMotor = Motor(Port.B)
RMotor = Motor(Port.C)
US = UltrasonicSensor(Port.S4)
CS = ColorSensor(Port.S3)
ARM = Motor(Port.D)
robot = DriveBase(LMotor, RMotor, wheel_diameter=50, axle_track=126)
#Calibrate these values. Do not share with anyone!!! 
# Calculate the light threshold. Choose values based on your measurements.
black = 8
white = 44
threshold = (black+white)/2
green = 8,9,10,11

# Start following the line endlessly.
while CS.color != Color.RED: 
    ARM.run(1000)
    if CS.reflection() < threshold:
        robot.drive(45,50)
     
    else:
         robot.drive(45,-50)
    if CS.color == green:
        robot.straight(10)