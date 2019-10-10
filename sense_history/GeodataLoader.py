from shapely.geometry import shape
from functools import reduce
import operator
import json
import yaml


class GeodataLoader(object):

    MODULES_CONFIG = './module/config.yml'
    MODULES = ['BERLIN_WALL', 'ZURICH_TREES']

    def __init__(self, MODULE_NAME):
        assert MODULE_NAME in self.MODULES
        with open(self.MODULES_CONFIG) as f:
            self.cfg = yaml.load(f, Loader=yaml.FullLoader)[MODULE_NAME]
        self.load_module(MODULE_NAME)
        

    def load_module(self, MODULE):
        if MODULE == 'BERLIN_WALL':
            self.data = self.load_polygon()
        if MODULE == 'ZURICH_TREES':
            self.data = self.load_json()

    def load_json(self):
        data = self.load_json(self.cfg['path'])[self.cfg['key']]
        data = data[:100]
        features = [self.extract_features(record) for record in data]

    def load_polygon(self):
        with open(self.cfg['path']) as f:
            data = json.load(f)
        return shape(data['features'][0]['geometry'])

    def load_json(self, path):
        with open(path) as f:
            data = json.load(f)
        return data

    def extract_features(self, record):
        latitude = self.get_from_dictionary(record, self.cfg['latitude'])
        longitude = self.get_from_dictionary(record, self.cfg['longitude'])
        features = {} 
        for feature in self.cfg['features']:
            properties = self.get_from_dictionary(record, feature.values()[0])
            features.update({feature.keys()[0]: properties})

    def get_from_dictionary(self, data, keys):
        return reduce(operator.getitem, keys, data)





