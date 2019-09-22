from shapely.geometry import shape
import json


class GeodataLoader(object):

    def __init__(self):
        pass

    def load_polygon(self, path):
        with open(path) as f:
            data = json.load(f)
        return shape(data['features'][0]['geometry'])
