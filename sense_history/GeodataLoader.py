from shapely.geometry import shape
from functools import reduce
import operator
import json
import yaml
import pdb

class GeodataLoader(object):

    MODULES_CONFIG = './module/config.yml'
    MODULES = ['BERLIN_WALL', 'BERLIN_HISTORIC', 'ZURICH_TREES']

    def __init__(self, MODULE_NAME):
        assert MODULE_NAME in self.MODULES
        with open(self.MODULES_CONFIG) as f:
            self.cfg = yaml.load(f, Loader=yaml.FullLoader)[MODULE_NAME]
        self.load_module(MODULE_NAME)
        

    def load_module(self, MODULE):
        if MODULE == 'BERLIN_WALL':
            self.data = self.load_polygon()
        if MODULE == 'BERLIN_HISTORIC':
            self.data = self.load_geojson()
        if MODULE == 'ZURICH_TREES':
            self.data = self.load_geojson()

    def load_geojson(self):
        data = self.load_json(self.cfg['path'])[self.cfg['key']]
        data = data[:100]
        features = [self.extract_features(record) for record in data]
        pdb.set_trace()

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
        features = {'latitude': latitude, 'longitude': longitude} 
        for feature in self.cfg['features']:
            properties = self.get_from_dictionary(record, feature.values()[0])
            features.update({feature.keys()[0]: properties})
        return features

    def get_from_dictionary(self, data, keys):
        try:
            return reduce(operator.getitem, keys, data)
        except:
            return ''


