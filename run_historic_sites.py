from sense_history.GeodataLoader import GeodataLoader
from sense_history.Vibrator import Vibrator
from sense_history.GPS import GPS
from shapely.geometry import Point
import logging
import time

MODULE: str = 'BERLIN_HISTORIC'
#MODULE = 'ZURICH_TREES'
RADIUS: float = 5.00

data = GeodataLoader(MODULE)

FORMAT = '%(asctime)-15s: %(message)s'
log_file = './logs/sense_history_trees.log'
log_file = './logs/sense_history_historic.log'
logging.basicConfig(format=FORMAT, level=logging.INFO, filename=log_file, filemode='a')
#logging.basicConfig(format=FORMAT, level=logging.INFO)

vibrator: Vibrator = Vibrator()
gps: GPS = GPS()
vibrator.stop()

logging.info('START POSITIONING')
i = 0
while True:

    logging.info('Location step: {}'.format(i))
    longitude, latitude = gps.get_position()
    position = Point(longitude, latitude)

    for poi in data.POIs:
        distance = poi.distance(position)
        if distance <= RADIUS:
            vibrator.run()
            break
            
    i += 1
    time.sleep(0.5)

gps.stop()
