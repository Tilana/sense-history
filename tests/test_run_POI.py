import unittest
from sense_history.GeodataLoader import GeodataLoader 
from shapely.geometry import Point

class TestRunConfig(unittest.TestCase):

    def setUp(self):
        MODULE = 'BERLIN_HISTORIC'
        self.POIs = GeodataLoader(MODULE).POIs

    def test(self):
        luftbrueckendenkmal = Point(13.3874049, 52.474135)
        
        distances = [poi.distance(luftbrueckendenkmal) for poi in self.POIs]
        print(distances[:10])
        distances.sort()
        print(distances[:10])
        close_POIs = [distance for distance in distances if distance <= 5]


        #self.assertEqual(len(close_POIs), 1)
        #fernsehturm = Point(13.409779, 52.520645)
        #self.assertFalse(self.berlin_wall.contains(fernsehturm))
        #stuttgart = Point(9.176514, 48.773079)
        #self.assertFalse(self.berlin_wall.contains(stuttgart))
        #siegessaeule = Point(13.350119, 52.514543)
        #self.assertTrue(self.berlin_wall.contains(siegessaeule))
        #westend = Point(13.259284, 52.508645)
        #self.assertTrue(self.berlin_wall.contains(westend))
        #checkpoint_charlie_west = Point(13.390391, 52.507443)
        #checkpoint_charlie_east = Point(13.390391, 52.508043)
        #self.assertTrue(self.berlin_wall.contains(checkpoint_charlie_west))
        #self.assertFalse(self.berlin_wall.contains(checkpoint_charlie_east))

        #self.assertTrue(self.berlin_wall.almost_equals(checkpoint_charlie_east, 1))
        #self.assertTrue(self.berlin_wall.almost_equals(checkpoint_charlie_west))

