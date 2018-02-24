import json
import requests

from grandpyapp.wikimedia import WikiMedia


class TestWikiMedia:

    latitude = 48.8747578
    longitude = 2.350564700000001
    title = "Cité Paradis"

    instance = WikiMedia(latitude, longitude, title)

    geosearch_file = 'mock_folder/wikimedia_geosearch_mock.json'
    with open(geosearch_file) as mock_file:
        _geosearch_json = json.load(mock_file)

    extract_file = 'mock_folder/wikimedia_extracts_mock.json'
    with open(extract_file) as mock_file:
        _extract_json = json.load(mock_file)

    def setup_metod(self):
        assert isinstance(instance, WikiMedia)

    def test_title(self):
        assert hasattr(self.instance, 'title') == True

    def test_page_id(self):
        assert hasattr(self.instance, 'page_id') == True

    def test_page_content(self):
        assert hasattr(self.instance, 'content') == True

    def test_geosearch(self, monkeypatch):

        def mockreturn(get, params):
            mockreturn = requests.Response()
            mockreturn.status_code = 200
            mockreturn._content = json.dumps(self._geosearch_json).encode()
            return mockreturn

        monkeypatch.setattr(requests, 'get', mockreturn)

        assert self.instance.geosearch() == self._geosearch_json

    def test_find_page_id(self):
        assert isinstance(self.instance.find_page_id(self._geosearch_json), int)

    def test_extract_content(self, monkeypatch):

        def mockreturn(get, params):
            mockreturn = requests.Response()
            mockreturn.status_code = 200
            mockreturn._content = json.dumps(self._extract_json).encode()
            return mockreturn

        monkeypatch.setattr(requests, 'get', mockreturn)

        assert self.instance.extract_content(5653202) == self._extract_json

    def test_get_contents(self):
        assert isinstance(self.instance.get_contents(self._extract_json), str)
