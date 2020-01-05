from sense_history.GeodataLoader import GeodataLoader
from sense_history.Vibrator import Vibrator
from sense_history.GPS import GPS
from shapely.geometry import Point
import logging
import time


def run_border(module: str, gps: GPS, vibrator: Vibrator) -> None:

    logging.info('LOAD DATA')
    west_sector = GeodataLoader(module).data
    
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
   
