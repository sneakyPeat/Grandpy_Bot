import requests
import json


class GoogleMaps:
    """
    This class is used to make a link between the google maps API and the programm.
    """

    def __init__(self, parsed_query):
        self.parsed_query = parsed_query

        # variable used for API
        # self.url = app.config['GM_GEOCODING_URL']
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json?address'
        self.key = '&key=' + 'AIzaSyDKGJ_R9HNsdkeHiC3W1cIZ8e2e2vzRqAc'
        # self.key = '&key=' + app.config['GM_GEOCODING_KEY']

        self.find_coordinates(self.url)

    def find_coordinates(self, url):

        response = requests.get(url, params=self.parsed_query + self.key)

        if response.status_code != requests.code.ok:
            response = response.raise_for_status()

        json_response = json.loads(response.read().decode('utf8'))


g = GoogleMaps("OpenClassrooms")
