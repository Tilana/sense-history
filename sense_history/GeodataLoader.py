from shapely.geometry import shape, Point
from functools import reduce
from POI import POI
import operator
import json
import yaml

class GeodataLoader(object):

    MODULES_CONFIG = './module/config.yml'
    MODULES = ['BERLIN_WALL', 'BERLIN_HISTORIC', 'ZURICH_TREES', 'TEST']

    def __init__(self, MODULE_NAME):
        assert MODULE_NAME in self.MODULES
        with open(self.MODULES_CONFIG) as f:
            self.cfg = yaml.load(f, Loader=yaml.FullLoader)[MODULE_NAME]
        self.load_module(MODULE_NAME)
        if 'filter' in self.cfg.keys():
            key, value = self.cfg['filter'].items()[0]
            self.filter(key, value)

    def load_module(self, MODULE):
        if MODULE == 'BERLIN_WALL':
            self.data = self.load_polygon()
        if MODULE == 'BERLIN_HISTORIC':
            self.data = self.load_geojson()
        if MODULE == 'ZURICH_TREES':
            self.data = self.load_geojson()

    def load_geojson(self):
        data = self.load_json(self.cfg['path'])[self.cfg['key']]
        self.POIs = [self.extract_features(record) for record in data]

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
        poi = POI('POI', latitude, longitude)
        features = self.cfg['features']
        for key in features.keys():
            properties = self.get_from_dictionary(record, features[key])
            poi.add_feature(key, properties)
        return poi

    def get_from_dictionary(self, data, keys):
        try:
            return reduce(operator.getitem, keys, data)
        except:
            return ''

    def filter(self, key, value):
        # TODO: Make this function more applicable to other use cases, e.g. filter by strings, etc.
        self.POIs = [POI for POI in self.POIs if (getattr(POI, key) != None) and (int(getattr(POI, key)) <= value)]


