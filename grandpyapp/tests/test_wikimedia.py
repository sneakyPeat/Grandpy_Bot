import json
import requests

from grandpyapp.WikiMedia import WikiMedia


class TestWikiMedia:

    latitude = 48.8747578
    longitude = 2.350564700000001
    title = "Cité Paradis"

    instance = WikiMedia(latitude, longitude, title)


    def setup_metod(self):
        assert isinstance(instance, WikiMedia)

    def test_geosearch(self, monkeypatch):

        json_file = 'mock_folder/wikimedia_mock.json'
        with open(json_file) as mock_file:
            results = json.load(mock_file)

        def mockreturn(get, params):
            mockreturn = requests.Response()
            mockreturn.status_code = 200
            mockreturn._content = json.dumps(results).encode()
            return mockreturn

        monkeypatch.setattr(requests, 'get', mockreturn)

        assert self.instance.geosearch() == result
