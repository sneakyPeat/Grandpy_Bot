from grandpyapp.query import Query

import json


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
        It must returned a list of 3 elements  with at at least 1 element"""
        assert len(self.instance.parse_question()) > 0

    def test_collect_data(self):
        assert isinstance(self.instance.create_json(), dict)
