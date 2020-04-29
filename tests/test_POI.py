import unittest

from sense_history.POI import POI
from sense_history.POI import DD_METER 
from shapely.geometry import Point



class TestPOI(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        poi = POI('Test POI', 42.00, 10.00)
        self.assertEqual(poi.id, 'Test POI')
        self.assertEqual(poi.location.x, 10.00)
        self.assertEqual(poi.location.y, 42.00)

    def test_distance_degrees(self):
        poi = POI('Test POI', longitude=3.00, latitude=0.00)
        self.assertEqual(poi.distance(Point(0.00, 0.00), unit='degree'), 3.00)
        self.assertEqual(poi.distance(Point(0.00, 4.00), unit='degree'), 5.00)
    
    def test_distance_meter_longitude(self):
        equator = POI('equator', longitude=0.00, latitude=0.00)
        # At the equator a degree of longitude is constant
        self.assertEqual(equator.distance(Point(1.00, 0.00), unit='meter'), DD_METER)
        self.assertEqual(equator.distance(Point(5.00, 0.00), unit='meter'), DD_METER * 5)
        # the closer to the poles the smaller a degree of longitude in meters 
        lat_30 = POI('lat 30', longitude=0.00, latitude=30)
        lat_50 = POI('lat 50', longitude=0.00, latitude=50)
        lat_70 = POI('lat 70', longitude=0.00, latitude=70)
        dist_30 = lat_30.distance(Point(1, 30), unit='meter')
        dist_50 = lat_50.distance(Point(1, 50), unit='meter')
        dist_70 = lat_70.distance(Point(1, 70), unit='meter')
        self.assertTrue(dist_30 > dist_50 and dist_50 > dist_70)
        # At the poles a degree of longitude is zero 
        northpole = POI('Northpole', longitude=0.00, latitude=90.0)
        self.assertAlmostEqual(northpole.distance(Point(1.00, 90.00), unit='meter'), 0)
        # TODO: Make functions work for southern hemisphere
        # southpole = POI('Southpole', longitude=0.00, latitude=-90.0)
        # self.assertAlmostEqual(northpole.distance(Point(1.00, -90.00), unit='meter'), 0)

    def test_distance_meter_latitude(self):
        # One latitude degree in meter is always constant
        lon_30 = POI('lon 30', longitude=30.00, latitude=0)
        lon_50 = POI('lon 50', longitude=50.00, latitude=0)
        lon_70 = POI('lon 70', longitude=70.00, latitude=0)
        dist_30 = lon_30.distance(Point(30, 1), unit='meter')
        dist_50 = lon_50.distance(Point(50, 1), unit='meter')
        dist_70 = lon_70.distance(Point(70, 1), unit='meter')
        self.assertAlmostEqual(dist_30, DD_METER)
        self.assertAlmostEqual(dist_30, dist_50)
        self.assertAlmostEqual(dist_50, dist_70)


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

