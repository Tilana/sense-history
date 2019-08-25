#!/usr/bin/python
# -*- coding:utf-8 -*-

from sense_history import Vibrator, GPS
import logging
import time

FORMAT = '%(asctime)-15s: %(message)s'
logging.basicConfig(format=FORMAT)
logging.getLogger().setLevel(logging.INFO)

vibrator = Vibrator()
gps = GPS()
vibrator.stop()

print('START POSITIONING')
for i in range(35):
    longitude, latitude = gps.get_position()
    time.sleep(0.5)

    if i % 5 == 0:
        vibrator.run()

gps.stop()

