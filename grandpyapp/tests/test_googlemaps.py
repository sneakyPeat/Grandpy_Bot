import json
import requests
from grandpyapp.GoogleMaps import GoogleMaps


class TestGoogleMaps:

    instance = GoogleMaps("OpenClassrooms")

    def setup_metod(self):
        assert isinstance(self.instance, GoogleMaps)

    def test_latitude(self):
        assert self.instance.hasattr('latitude') == True

    def test_longitude(self):
        assert self.instance.hasattr('longitude') == True

    def test_adresse(self):
        assert self.instance.hasattr('adress') == True

    def test_find_coordinates(self, monkeypatch):

        json_file = "mock_folder/gmaps_results_mock.json"
        with open(json_file) as mock_file:
            results = json.load(mock_file)

        def mockreturn(get, params):
            mockreturn = requests.Response()
            mockreturn.status_code = 200
            mockreturn._content = json.dumps(results).encode()
            return mockreturn

        monkeypatch.setattr(requests, 'get', mockreturn)

        assert self.instance.find_coordinates() == results
