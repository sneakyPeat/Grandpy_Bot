import json
import request
import os
from io import BytesIO


class TestGoogleMaps:
    def setup_metod(self):
        self.query = "OpenClassrooms"
        self.instance = GoogleMaps(self.query)
        assert isinstance(self.instance, GoogleMaps)

    def test_find_coordinates(self):

        with open("mock_folder/gmaps_results_mock.json") as mock_file:
            results = json.load(mock_file)

        def mockreturn(request):
            return BytesIO(json.dumps(results).encode())

        monkeypatch.setattr(request, 'get', mockreturn)

        assert self.instance.find_coordinates == results
