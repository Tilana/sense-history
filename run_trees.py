import json
from sense_history import GeodataLoader
from sense_history import Vibrator, GPS
import pandas as pd
import logging
import pdb
import math

PATH = './module/zurich-baeume/baumkataster.json'

with open(PATH) as f:
    data = json.load(f)


def extract_info(record):
    latitude = record['geometry']['coordinates'][1]
    longitude = record['geometry']['coordinates'][0]
    category = record['properties']['kategorie']
    tree_type = record['properties']['baumnamedeu']
    year = record['properties']['pflanzjahr']
    return {'latitude': latitude, 'longitude': longitude, 'category': category,
            'tree_type': tree_type, 'year': year}


all_trees = [extract_info(record) for record in data['features']]
all_trees = pd.DataFrame(all_trees)
all_trees['year'] = pd.to_numeric(all_trees['year'], errors='coerce')

old_trees = all_trees[all_trees.year <= 1969]

FORMAT = '%(asctime)-15s: %(message)s'
log_file = './logs/sense_history_trees.log'
logging.basicConfig(format=FORMAT, level=logging.INFO, filename=log_file, filemode='a')

vibrator = Vibrator()
gps = GPS()
vibrator.stop()

logging.info('START POSITIONING')
i = 0
while True:

    logging.info('Location step: {}'.format(i))
    longitude, latitude = gps.get_position()
    pdb.set_trace()
    current_position = Point(longitude, latitude)

    if math.isclose(current_position, tree_positions):
        vibrator.run()
    i += 1
    time.sleep(0.5)

gps.stop()


pdb.set_trace()
