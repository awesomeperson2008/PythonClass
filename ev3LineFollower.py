#!/usr/bin/env python3

from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_D
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import button
from time import sleep

btn = Button()
tank_pair = MoveTank(OUTPUT_A, OUTPUT_D)

c1 = ColorSensor()

while not btn.any():
    if c1.reflected_light_intensity < 25:
        tank_pair.on(left_speed = 50, right_speed = 0)

    else:
        tank_pair.on(left_speed = 0, right_speed = 50)

    sleep(0.1)

