import unittest

from sense_history.POI import POI
from shapely.geometry import Point


class TestPOI(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        poi = POI('Test POI', 42.00, 10.00)
        self.assertEqual(poi.id, 'Test POI')
        self.assertEqual(poi.location.x, 10.00)
        self.assertEqual(poi.location.y, 42.00)

    def test_distance(self):
        poi = POI('Test POI', longitude=3.00, latitude=0.00)
        self.assertEqual(poi.distance(Point(0.00, 0.00), False), 3.00)
        self.assertEqual(poi.distance(Point(0.00, 4.00), False), 5.00)

    def test_intermediaryPoints(self):
        start = POI('Start', longitude=2.00, latitude=0.00)
        end = Point(5.00, 0.00)
        intermediary_points = [start.location,
                               Point(3.00, 0.00),
                               Point(4.00, 0.00),
                               end]
        self.assertEqual(start.intermediary_points(end), intermediary_points)
        
        start = POI('Start', longitude=2.00, latitude=0.00)
        end = Point(5.00, 4.00)
        intermediary_points = [start.location,
                               Point(2.6, 0.8),
                               Point(3.2, 1.6),
                               Point(3.8, 2.4),
                               Point(4.4, 3.2),
                               end]
        self.assertEqual(start.intermediary_points(end), intermediary_points)


        start = POI('Start', longitude=4.00, latitude=0.00)
        end = Point(0.00, 3.00)
        intermediary_points = [start.location,
                               Point(3.2, 0.6),
                               Point(2.4, 1.2),
                               Point(1.6, 1.8),
                               Point(0.8, 2.4),
                               end]
        self.assertEqual(start.intermediary_points(end), intermediary_points)
        


if __name__== '__main__':
    unittest.main()

