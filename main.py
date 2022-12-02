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
sensor = InfraredSensor(Port.S4)
motorLinks = Motor(Port.A)
motorRechts = Motor(Port.D)

# Write your program here.
ev3.speaker.beep()
print("Programm Startet")
while True:
  if sensor.buttons(1) == [Button.LEFT_UP]:
    print("Links UP")
    motorLinks.dc(100)
    wait(200)
  if sensor.buttons(1) == [Button.LEFT_DOWN]:
    print("Links DOWN")
    motorLinks.dc(-100)
    wait(200)
  if sensor.buttons(1) == [Button.RIGHT_UP]:
    print("Rechts UP")
    motorRechts.dc(100)
    wait(200)
  if sensor.buttons(1) == [Button.RIGHT_DOWN]:
    print("Rechts DOWN")
    motorRechts.dc(-100)
    wait(200)
  if sensor.buttons(1) == [Button.LEFT_DOWN, Button.RIGHT_DOWN]:
    print("Beide DOWN")
    motorRechts.dc(-100)
    motorLinks.dc(-100)
    wait(200)
  if sensor.buttons(1) == [Button.LEFT_UP, Button.RIGHT_UP]:
    print("Beide UP")
    motorRechts.dc(100)
    motorLinks.dc(100)
    wait(200)
  if sensor.buttons(1) == [Button.LEFT_UP, Button.RIGHT_DOWN]:
    print("Drehung Rechts")
    motorRechts.dc(-100)
    motorLinks.dc(100)
    wait(200)
  if sensor.buttons(1) == [Button.LEFT_DOWN, Button.RIGHT_UP]:
    print("Drehung Links")
    motorRechts.dc(100)
    motorLinks.dc(-100)
    wait(200)
  if sensor.buttons(1) == []:
    print("Stop")
    motorLinks.dc(0)
    motorRechts.dc(0)
    wait(200)
