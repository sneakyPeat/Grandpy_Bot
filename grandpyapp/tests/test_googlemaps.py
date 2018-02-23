import json
import requests

from grandpyapp.GoogleMaps import GoogleMaps


class TestGoogleMaps:

    instance = GoogleMaps("OpenClassrooms")

    def setup_metod(self):
        assert isinstance(self.instance, GoogleMaps)

    def test_find_coordinates(self, monkeypatch):

        json_file = "mock_folder/gmaps_results_mock.json"
        with open(json_file) as mock_file:
            results = json.load(mock_file)
            print(type(results), "results")

        def mockreturn(get, params):
            return results

        monkeypatch.setattr(requests, 'get', mockreturn)

        assert self.instance.find_coordinates() == result
