from sense_history.GeodataLoader import GeodataLoader
from sense_history.Vibrator import Vibrator
from sense_history.GPS import GPS
from shapely.geometry import Point
import logging
import time


def run_POIs(module: str, gps: GPS, vibrator: Vibrator, radius: float) -> None:

    logging.info('LOAD DATA')
    data = GeodataLoader(module)

    logging.info('START POSITIONING')
    i = 0
    while True:
    
        logging.info('Location step: {}'.format(i))
        longitude, latitude = gps.get_position()
        position = Point(longitude, latitude)
    
        for poi in data.POIs:
            distance = poi.distance(position)
            if distance <= radius:
                vibrator.run()
                break
                
        i += 1
        time.sleep(0.5)
    
    gps.stop()
