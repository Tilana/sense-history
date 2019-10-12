#!/usr/bin/python
# -*- coding:utf-8 -*-
from sense_history import GeodataLoader
from sense_history import Vibrator, GPS
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

PATH = './module/berlin-wall/polygon.geojson'
west_sector = GeodataLoader().load_polygon(PATH)

was_in_west = False

logging.info('START POSITIONING')
i = 0
while True:

    logging.info('Location step: {}'.format(i))
    longitude, latitude = gps.get_position()
    current_position = Point(longitude, latitude)
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

