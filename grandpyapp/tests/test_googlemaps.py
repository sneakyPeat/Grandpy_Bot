import json
import requests
from grandpyapp.GoogleMaps import GoogleMaps


class TestGoogleMaps:

    instance = GoogleMaps("OpenClassrooms")

    def setup_metod(self):
        assert isinstance(self.instance, GoogleMaps)

    def test_title(self):
        assert isinstance(self.instance.title, str)

    def test_latitude(self):
        assert isinstance(self.instance.latitude, float)

    def test_longitude(self):
        assert isinstance(self.instance.longitude, float)

    def test_address(self):
        assert isinstance(self.instance.address, str)

    def test_find_coordinates(self, monkeypatch):

        json_file = "grandpyapp/tests/mock_folder/gmaps_results_mock.json"
        with open(json_file) as mock_file:
            results = json.load(mock_file)

        def mockreturn(get, params):
            mockreturn = requests.Response()
            mockreturn.status_code = 200
            mockreturn._content = json.dumps(results).encode()
            return mockreturn

        monkeypatch.setattr(requests, 'get', mockreturn)

        assert self.instance.find_coordinates() == results
