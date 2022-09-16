#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
color_sensor = ColorSensor(Port.S3)
spin_motor = Motor(Port.D)

#Begin Drivebase
robot = DriveBase(right_motor, left_motor, wheel_diameter=55.5, axle_track=104)

#Main
while True:
  robot.drive(40,0)
  if color_sensor.reflection() > 30:
    robot.straight(120)
    else:
     robot.drive(-30,50)
     elif color.reflection() == 5:
      robot.exit
      
while True:
  spin_motor.run_target(1000, 36000)
