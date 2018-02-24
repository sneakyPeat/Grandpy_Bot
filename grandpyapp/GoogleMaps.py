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

        coord = self.find_coordinates()

        self._title = coord["results"][0]["address_components"][1]["long_name"]
        self._address = coord["results"][0]["formatted_address"]
        self._lat = coord["results"][0]["geometry"]["location"]["lat"]
        self._lng = coord["results"][0]["geometry"]["location"]["lng"]

    @property
    def title(self):
        return self._title
    @property
    def address(self):
        return self._address
    @property
    def latitude(self):
        return self._lat
    @property
    def longitude(self):
        return self._lng

    def find_coordinates(self):
        params = {'address': self._parsed_query, 'key': self._key}
        response = requests.get(self._url, params=params)
        # print(response.url)
        if response.status_code == requests.codes.ok:
            response = response.json()
        else:
            response = response.raise_for_status()
        return response
