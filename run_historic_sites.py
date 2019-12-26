from sense_history import GeodataLoader
from sense_history import Vibrator, GPS
from shapely.geometry import Point
import logging
import time

MODULE = 'BERLIN_HISTORIC'
MODULE = 'ZURICH_TREES'
RADIUS = 10 

data = GeodataLoader(MODULE)

FORMAT = '%(asctime)-15s: %(message)s'
log_file = './logs/sense_history_trees.log'
logging.basicConfig(format=FORMAT, level=logging.INFO, filename=log_file, filemode='a')
#logging.basicConfig(format=FORMAT, level=logging.INFO)

vibrator = Vibrator()
gps = GPS()
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
