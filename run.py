import json
from utils import load_polygon
from shapely.geometry import shape, Point
import pdb

PATH = './module/berlin-wall/polygon.geojson'

with open(PATH) as f:
    data = json.load(f)

point = Point(-122.7924463, 45.4519896)
polygon = shape(data['features'][0]['geometry'])

print(polygon.contains(point))

for feature in data['features']:
    print(feature['geometry']['type'])

pdb.set_trace()
