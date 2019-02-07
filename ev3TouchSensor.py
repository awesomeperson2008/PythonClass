#!/usr/bin/env python3
from ev3dev2.led import Leds
from ev3dev2.sensor.lego import TouchSensor
from time import sleep

leds = Leds()
ts = TouchSensor()

while True:
    if ts.is_pressed:
        leds.set_color('LEFT', 'RED')
    else:
        leds.set_color('LEFT', 'GREEN')

    sleep(0.1) # Give the CPU some rest
