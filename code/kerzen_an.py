#!/usr/bin/env python

from gpiozero import LED

stern = LED(15)

kerzen = [LED(18), LED(23), LED(24), LED(25), LED(8)]

stern.on()

for i in range(5):
    kerzen[i].on()

