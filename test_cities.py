import unittest
from city_function import city_country


class CityTestCase(unittest.TestCase):
    "test city_function.py"
    def test_city_country(self):
        formatted_name = city_country('Santiago', 'Chile')   # Expected
        self.assertEqual(formatted_name, 'Santiago Chile')   # Actual

    def test_city_country_population(self):
        formatted_name = city_country('Santiago', 'Chile', '5000')
        self.assertEqual(formatted_name, 'Santiago Chile-population 5000')

