from typing import List
from shapely.geometry import Point

DD_METER: float = 111.139

class POI:

    def __init__(self, id: str, latitude: float, longitude: float):
        self.id: str = id 
        self.location: Point = Point(longitude, latitude)

    def add_feature(self, key, value):
        setattr(self, key, value)

    def distance(self, position: Point, in_meter: bool = True):
        dist = self.location.distance(position)
        if in_meter:
            return dist * DD_METER
        return dist

    def intermediary_points(self, target_pos: Point, max_length: float = 1.0) -> List[Point]:
        dist = self.distance(target_pos, False)
        n = int(dist / max_length)
        
        x_diff = target_pos.x - self.location.x
        y_diff = target_pos.y - self.location.y

        x_diff_part = x_diff / float(n)
        y_diff_part = y_diff / float(n)

        points = [self.location]
        for i in range(1, n):
            points.append(Point(round(self.location.x + (x_diff_part * i), 6),
                                round(self.location.y + (y_diff_part * i), 6)))
        points.append(target_pos)
        return points

