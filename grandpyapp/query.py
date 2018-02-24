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
        self.create_json()

    def parse_question(self):
        """
        The query pass to the object Query might be from natural language, therefore it must have some words removed from the query. The file fr.json contains all the stopwords mandatory to remove from the query.
        """
        self.question = self.question.replace("\'", " ")
        json_file = '../data/fr.json'
        with open(json_file) as json_data:
            stopwords = json.load(json_data)

        translator = str.maketrans('', '', string.punctuation)
        question = self.question.translate(translator).split()

        for stopword in stopwords:
            for word in question:
                if word.lower() == stopword.lower():
                    question.remove(word)
        return question

    def create_json(self):
        url = "http://fr.wikipedia.org/?curid="
        json_data = {
        "query" : "",
        "google_api" : {
            "address" : "",
            "lat" : "",
            "lng" : ""
            },
        "wikimedia_api" : {
            "title" : "",
            "content" : "",
            "wiki_link" : ""
            }
        }

        parse_question = self.parse_question()
        json_data["query"] = self.question

        gm = GoogleMaps(parse_question)
        json_data['google_api']['address'] = gm.address
        json_data['google_api']['lat'] = gm.latitude
        json_data['google_api']['lng'] = gm.longitude
        title = gm.title

        wk =WikiMedia(gm.latitude, gm.longitude, gm.title)
        json_data['wikimedia_api']['title'] = wk.title
        json_data['wikimedia_api']['content'] = wk.content
        json_data['wikimedia_api']['wiki_link'] = url + str(wk.page_id)

        json_str = json.dumps(json_data, indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
        json_data = json.loads(json_str)

        return json_data
