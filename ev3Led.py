#!/usr/bin/env python3
from ev3dev2.led import Leds
from time import sleep

leds = Leds()

leds.all_off()
sleep(1)

leds.set_color('LEFT', 'AMBER')
leds.set_color('RIGHT', 'AMBER')
sleep(4)

#With custom color:
leds.set_color('LEFT', (1, 0)) # Bright RED
leds.set_color('RIGHT', (0, 1)) # Bright Green
sleep(4)



