from shapely.geometry import Point

DD_METER = 111.139

class POI:

    def __init__(self, id, latitude, longitude):
        self.id = id 
        self.location = Point(longitude, latitude)

    def add_feature(self, key, value):
        setattr(self, key, value)

    def distance(self, position):
        return self.location.distance(position) * DD_METER


