#!/usr/bin/env python2

from gpiozero import LED
from time import sleep
import os

led = LED(17)

while True:
        res = os.system("ping -c 1 google.de > /dev/null 2>&1")
        if res == 0:
                led.off()
                #print "is up!"
        else:
                led.blink(0.2, 0.2)
                #print "is down!"
        sleep(10)
