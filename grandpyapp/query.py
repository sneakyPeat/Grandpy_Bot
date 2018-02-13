import json
import string

from .views import app


class Query:
    """
    This class intend to manipulate the query from the user.
    """

    def __init__(self, question):
        """
        When a object is instancied, it must contains a query.
        The query is a string object.
        """
        self.question = question
        self.parse_question()

    def parse_question(self):
        """
        The query pass to the object Query might be from natural language, therefore it must have some words removed from the query. The file fr.json contains all the stopwords mandatory to remove from the query.
        """
        self.question = self.question.replace("\'", " ")
        stopwords = self.open_json("fr.json")
        translator = str.maketrans('', '', string.punctuation)
        question = self.question.translate(translator).split()

        for stopword in stopwords:
            for word in question:
                if word.lower() == stopword.lower():
                    question.remove(word)
        return question

    def open_json(self, filename):
        with open(filename) as json_data:
            stop_words = json.load(json_data)
        return stop_words


# q = Query("Salut grandpy! Tu connais l'adresse d'OpenClassrooms?")
