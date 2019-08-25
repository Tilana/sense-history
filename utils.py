from shapely.geometry import shape
import json

def load_polygon(path):
    with open(path) as f:
        data = json.load(f)

    return shape(data['features'][0]['geometry'])
