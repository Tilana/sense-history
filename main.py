from sense_history.GeodataLoader import GeodataLoader
from sense_history.Vibrator import Vibrator
from sense_history.GPS import GPS
from shapely.geometry import Point
import pdb
import logging
import time

FORMAT = '%(asctime)-15s: %(message)s'
log_file = './logs/sense_history.log'
logging.basicConfig(format=FORMAT, level=logging.INFO, filename=log_file, filemode='a')
#logging.basicConfig(format=FORMAT, level=logging.INFO) 

vibrator: Vibrator = Vibrator()
gps: GPS = GPS()
vibrator.stop()

MODULE = 'BERLIN_WALL'

west_sector = GeodataLoader(MODULE).data

was_in_west: bool = False
was_located: bool = False

logging.info('START POSITIONING')
i = 0
while True:

    logging.info('Location step: {}'.format(i))
    longitude, latitude = gps.get_position()
    current_position = Point(longitude, latitude)

    if not was_located and gps.islocated():
        vibrator.run()
        was_located = True 

    is_in_west: bool = west_sector.contains(current_position)
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

