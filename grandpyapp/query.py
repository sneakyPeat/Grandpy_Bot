import json
import string
# from grandpyapp.views import app
#from GoogleMaps import GoogleMaps
#from wikimedia import WikiMedia
from grandpyapp.GoogleMaps import GoogleMaps
from grandpyapp.wikimedia import WikiMedia


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

    def parse_question(self):
        """
        The query pass to the object Query might be from natural language, therefore it must have some words removed from the query. The file fr.json contains all the stopwords mandatory to remove from the query.
        """
        self.question = self.question.replace("\'", " ")
        json_file = 'grandpyapp/data/fr.json'
        with open(json_file) as json_data:
            stopwords = json.load(json_data)

        translator = str.maketrans('', '', string.punctuation)
        question = self.question.translate(translator).split()

        for stopword in stopwords:
            for word in question:
                if word.lower() == stopword.lower():
                    question.remove(word)
        return question

    def collect_data(self):
        url = "http://fr.wikipedia.org/?curid="
        data = {}

        parse_question = self.parse_question()
        data["query"] = self.question

        gm = GoogleMaps(parse_question)
        data['address'] = gm.address
        data['lat'] = gm.latitude
        data['lng'] = gm.longitude

        wk = WikiMedia(gm.latitude, gm.longitude, gm.title)
        data['title'] = wk.title
        data['content'] = wk.content
        data['wiki_link'] = url + str(wk.page_id)

        return data
