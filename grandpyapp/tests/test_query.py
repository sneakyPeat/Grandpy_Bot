from grandpyapp.query import Query

import json


class TestQuery:
    def setup_method(self):
        """Test if the object created is an instance of the query class."""
        self.query = "Salut Grandpy! Est ce que tu connais l'adresse d'OpenClassrooms?"
        self.instance = Query(self.query)
        assert isinstance(self.instance, Query)

    def test_parser_method(self):
        """Test the parse method in the Query class. It must returned at least 1 element."""
        assert len(self.instance.parse_question()) == 1

    def test_collect_data(self):
        assert isinstance(self.instance.collect_data(), dict)
