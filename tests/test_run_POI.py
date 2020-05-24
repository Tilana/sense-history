import unittest
from sense_history.GeodataLoader import GeodataLoader
from shapely.geometry import Point

class TestRunConfig(unittest.TestCase):

    def setUp(self):
        MODULE = 'TEST'
        self.POIs = GeodataLoader(MODULE).POIs

    # TODO:
    # Requirements:
    # (1) Vibrate if close to POI
    # (2) Stop vibrating if constantly within radius of POI
    # (3) If out of radius of POI and in again vibrate

    def test_module(self):
        self.assertEqual(len(self.POIs), 5)
        names = [poi.name for poi in self.POIs]
        self.assertIn('Zuse Z3', names)

    def test(self):
        zuse_location = [poi.location for poi in self.POIs if poi.name == 'Zuse Z3'][0]
        distances = [poi.distance(zuse_location) for poi in self.POIs]
        self.assertIn(0, distances)
        for dist in distances:
            if dist != 0:
                self.assertGreaterEqual(dist, 3000)
        close_POIs = [distance for distance in distances if distance <= 5]
        self.assertEqual(len(close_POIs), 1)
