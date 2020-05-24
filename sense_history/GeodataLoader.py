from shapely.geometry import shape, Point
from typing import Dict, List
from functools import reduce
from sense_history.POI import POI
import operator
import json
import yaml
import pdb

class GeodataLoader(object):

    MODULES_CONFIG = './module/config.yml'
    MODULES = ['BERLIN_WALL', 'BERLIN_HISTORIC', 'ZURICH_TREES', 'TEST']

    def __init__(self, MODULE_NAME: str) -> None:
        assert MODULE_NAME in self.MODULES
        with open(self.MODULES_CONFIG) as f:
            self.cfg = yaml.load(f, Loader=yaml.FullLoader)[MODULE_NAME]
        self.load_module(MODULE_NAME)
        if 'filter' in self.cfg.keys():
            key, value = self.cfg['filter'].items()[0]
            self.filter(key, value)

    def load_module(self, MODULE: str) -> None:
        if MODULE == 'BERLIN_WALL':
            self.data = self.load_polygon()
        if MODULE == 'BERLIN_HISTORIC':
            self.load_geojson()
        if MODULE == 'ZURICH_TREES':
            self.load_geojson()
        if MODULE == 'TEST':
            self.load_geojson()

    def load_geojson(self) -> None:
        data = self.load_json(self.cfg['path'])[self.cfg['key']]
        data = data[:100]
        self.POIs = [self.extract_features(record) for record in data]

    def load_polygon(self) -> shape:
        with open(self.cfg['path']) as f:
            data = json.load(f)
        return shape(data['features'][0]['geometry'])

    def load_json(self, path: str) -> Dict:
        with open(path) as f:
            data = json.load(f)
        return data

    def extract_features(self, record: Dict):
        latitude = self.get_from_dictionary(record, self.cfg['latitude'])
        longitude = self.get_from_dictionary(record, self.cfg['longitude'])
        poi = POI('POI', latitude, longitude)
        features = self.cfg['features']
        for key in features.keys():
            properties = self.get_from_dictionary(record, features[key])
            poi.add_feature(key, properties)
        return poi

    def get_from_dictionary(self, data: Dict, keys: List):
        try:
            return reduce(operator.getitem, keys, data)
        except:
            return ''

    def filter(self, key, value) -> None:
        # TODO: Make this function more applicable to other use cases, e.g. filter by strings, etc.
        self.POIs = [POI for POI in self.POIs if (getattr(POI, key) != None) and (int(getattr(POI, key)) <= value)]

