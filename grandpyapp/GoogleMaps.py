import requests


class GoogleMaps:
    """
    This class is used to make a link between the google maps API and the programm.
    """

    def __init__(self, parsed_query):
        self._parsed_query = parsed_query

        # variable used for API
        # self._url = app.config['GM_GEOCODING_URL']
        self._url = 'https://maps.googleapis.com/maps/api/geocode/json'
        self._key = 'AIzaSyDKGJ_R9HNsdkeHiC3W1cIZ8e2e2vzRqAc'
        # self._key = app.config['GM_GEOCODING_KEY']

        self.find_coordinates()

    def find_coordinates(self):
        params = {'address': self._parsed_query, 'key': self._key}
        response = requests.get(self._url, params=params)

        if response.status_code == requests.codes.ok:
            response = response.json()
            print(response.values())
        else:
            response = response.raise_for_status()
        return response


# g = GoogleMaps("OpenClassrooms")
