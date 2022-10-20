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
supersonic_sensor = UltrasonicSensor(Port.S4)
CS = ColorSensor(Port.S3)
ARM = Motor(Port.D)
robot = DriveBase(LMotor, RMotor, wheel_diameter=50, axle_track=126)
#Calibrate these values. Do not share with anyone!!! 
# Calculate the light threshold. Choose values based on your measurements.
black = 8
white = 44
threshold = (black+white)/2
green_square = 0
green_square_number = 0

# Start following the line endlessly.
while CS.color != Color.RED: 
    ARM.run(500)
    if CS.reflection() < threshold:
        robot.drive(45,-50)
     
    else:
         robot.drive(45,50)
    if CS.color == Color.GREEN:
        robot.drive(30, 80)

        if green_square_number <= 1:
            robot.drive(30, 80)
        if CS.reflection() < threshold:
            robot.drive(30, 80)
        if CS.reflection() > threshold:
            robot.drive(30, 80)
        
    if CS.color() == Color.GREEN:
        green_square = 1
        if CS.color() != Color.GREEN and green_square_number == 1 and CS.reflection() > 20:
            green_square = 0
            green_square_number = green_square_number + 1
        
        while green_square_number == 2:
            ev3.speaker.beep()
            ev3.speaker.beep()
            ev3.speaker.beep()


        
        
        
        
        
        
        
        #CS.color() == Color.GREEN:
         #   checkpoints += 1

          #  if checkpoints == 7:
           ##    robot.turn(180)
