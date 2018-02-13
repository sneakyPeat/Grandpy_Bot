from .. import Query

import json

from io import BytesIO


class TestQuery:
    def setup_method(self):
        """
        Test if the object created is an instance of the query class
        """
        self.query = "Salut Grandpy! Est ce que tu connais l'adresse d'OpenClassrooms?"
        self.instance = Query(self.query)
        assert isinstance(self.instance, Query)

    def test_parser_method(self):
        """
        Test the parse method in the Query class.
        It must returned a list of 3 elements.
        """
        assert len(self.instance.parse_question()) == 3

    def test_api_gmaps(self, monkeypatch):
        results = [{
            "formatted_address": "7 Cité Paradis, 75010 Paris, France",
            "geometry": {
                "location": {
                    "lat": 48.8747578,
                    "lng": 2.350564700000001
                },
            }
        }]

        def mockreturn(request):
            return BytesIO(json.dumps(results).encode())
