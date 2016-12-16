#!/usr/bin/env python

from gpiozero import PWMLED, LED
from gpiozero.tools import random_values
from signal import pause

stern = LED(15)

kerzen = [PWMLED(18), PWMLED(23), PWMLED(24), PWMLED(25), PWMLED(8)]

stern.on()

for i in range (5):
    kerzen[i].source = random_values()

pause()
