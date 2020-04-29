import unittest
from sense_history.GeodataLoader import GeodataLoader 


class TestGeodataLoader(unittest.TestCase):

    def setUp(self):
        self.loader = GeodataLoader('TEST')

    def test_getFromDictionary(self):
        data = {'geometry': {'type': 'Point', 'coordinates': [42.00, 12.00]},
                'properties': {'name': 'POI', 'year': '1900'}}

        self.assertEqual(self.loader.get_from_dictionary(data, ['properties', 'name']), 'POI')
        self.assertEqual(self.loader.get_from_dictionary(data, ['geometry']), {'type': 'Point', 'coordinates': [42.00, 12.00]})

        LNG_keys = ['geometry', 'coordinates', 0]
        self.assertEqual(self.loader.get_from_dictionary(data, LNG_keys), 42.00)

        

if __name__ == '__main__':
    unittest.main()
