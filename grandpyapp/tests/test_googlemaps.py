import json
import urllib.request
from io import BytesIO


class TestGoogleMaps:
    def setup_metod(self):
        self.query = "Salut Grandpy! Est ce que tu connais l'adresse d'OpenClassrooms?"
        self.instance = GoogleMaps(self.query)
        assert isinstance(self.instance, GoogleMaps)

    def test_find_coordinates(self):
        with open("gmaps_resulst_mock.json") as mock_file:
            results = json.load(mock_file)

        def mockreturn(request):
            return BytesIO(json.dumps(results).encode())

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

        assert self.instance.find_coordinates == results
