from shapely.geometry import Point

DD_METER: float = 111.139

class POI:

    def __init__(self, id: str, latitude: float, longitude: float):
        self.id: str = id 
        self.location: Point = Point(longitude, latitude)

    def add_feature(self, key, value):
        setattr(self, key, value)

    def distance(self, position: Point):
        return self.location.distance(position) * DD_METER


