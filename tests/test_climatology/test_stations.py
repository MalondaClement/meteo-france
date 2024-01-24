#
#  tests/test_stations.py
#
#  Created by Clément Malonda on 19/01/2024.

import unittest

import requests

from meteo_france.climatology.stations import get_6m_stations_list, get_hourly_stations_list, get_daily_stations_list

class TestStations(unittest.TestCase):

    def test_get_6m_stations_list_result(self):
        result = get_6m_stations_list(94)
        theorical_result = {"id": "94042001", "nom": "JOINVILLE", "posteOuvert": True, "typePoste": 2, "lon": 2.462667, "lat": 48.813667, "alt": 37, "postePublic": True}
        self.assertEqual(result[0], theorical_result)

    def test_get_6m_stations_list_param_error(self):
        with self.assertRaises(requests.exceptions.HTTPError) as context:
            result = get_6m_stations_list(0)
            print(str(context.exception))
        self.assertEqual(str(context.exception), "404 Client Error: Not Found for url: https://public-api.meteofrance.fr/public/DPClim/v1/liste-stations/infrahoraire-6m?id-departement=0")
    
    def test_get_hourly_stations_list_result(self):
        result = get_hourly_stations_list(94)
        theorical_result = {"id": "94015002", "nom": "BRY-SPC", "posteOuvert": True, "typePoste": 5, "lon": 2.522667, "lat": 48.8335, "alt": 90, "postePublic": True}
        self.assertEqual(result[0], theorical_result)

    def test_get_hourly_list_param_error(self):
        with self.assertRaises(requests.exceptions.HTTPError) as context:
            result = get_hourly_stations_list(0)
            print(str(context.exception))
        self.assertEqual(str(context.exception), "404 Client Error: Not Found for url: https://public-api.meteofrance.fr/public/DPClim/v1/liste-stations/horaire?id-departement=0")

    def test_get_daily_stations_list_result(self):
        result = get_daily_stations_list(94)
        theorical_result = {"id": "94004001", "nom": "BOISSY-ST-LEGER", "posteOuvert": False, "typePoste": 4, "lon": 2.515, "lat": 48.75, "alt": 95, "postePublic": True}
        self.assertEqual(result[0], theorical_result)

    def test_get_daily_stations_list_param_error(self):
        with self.assertRaises(requests.exceptions.HTTPError) as context:
            result = get_daily_stations_list(0)
            print(str(context.exception))
        self.assertEqual(str(context.exception), "404 Client Error: Not Found for url: https://public-api.meteofrance.fr/public/DPClim/v1/liste-stations/quotidienne?id-departement=0")

if __name__ == "__main__":
    unittest.main()