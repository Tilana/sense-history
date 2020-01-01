#!/usr/bin/python
# -*- coding:utf-8 -*-
from sense_history.GeodataLoader import GeodataLoader
from sense_history.Vibrator import Vibrator
from sense_history.GPS import GPS
from shapely.geometry import Point
import logging
import time

FORMAT = '%(asctime)-15s: %(message)s'
log_file = './logs/sense_history.log'
logging.basicConfig(format=FORMAT, level=logging.INFO, filename=log_file, filemode='a')
#logging.basicConfig(format=FORMAT, level=logging.INFO) 

vibrator = Vibrator()
gps = GPS()
vibrator.stop()

MODULE = 'BERLIN_WALL'

west_sector = GeodataLoader(MODULE).data

was_in_west = False
was_located = 0

logging.info('START POSITIONING')
i = 0
while True:

    logging.info('Location step: {}'.format(i))
    longitude, latitude = gps.get_position()
    current_position = Point(longitude, latitude)

    if gps.islocated() - was_located == 1:
        vibrator.run()
        was_located = 1

    is_in_west = west_sector.contains(current_position)
    logging.info('in west: {}'.format(is_in_west))

    if is_in_west != was_in_west:
        if was_in_west:
            vibrator.run()
        else:
            vibrator.run()
            time.sleep(0.25)
            vibrator.run()

    was_in_west = is_in_west
    i += 1
    time.sleep(0.5)

gps.stop()

