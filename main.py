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
  line_sensor = ColorSensor(Port.S3)
  spin_motor = Motor(Port.D)

  #Begin Drivebase
  robot = DriveBase(right_motor, left_motor, wheel_diameter=55.5, axle_track=104)


  #Main

  #Start Motor
while True:
    spin_motor.run_target(1000, 36000)

#Calcualte Light Threshold     
BLACK = 9
WHITE = 85
threshold = (BLACK + WHITE) / 2

#Set the Drive Speed
DRIVE_SPEED = 100

#Proportional Gain for Line Control
PROPORTIONAL_GAIN = 1.2


    #Line Sensor
while True:

  #Calculate Deviation from Line
   deviation = line_sensor.reflection() - threshold

   #Calculate Turn Rate
    turn_rate = PROPORTIONAL_GAIN * deviation

    #Set the Drive base speed and turn rate
    robot.drive(DRIVE_SPEED, turn_rate)

    wait(10)

        
  while True:
    spin_motor.run_target(1000, 36000)
