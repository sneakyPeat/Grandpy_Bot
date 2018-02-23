import requests


class WikiMedia:

    def __init__(self, latitude, longitude, title):
        self._latitude = str(latitude)
        self._longitude = str(longitude)
        self._title = title

        self._url = 'https://fr.wikipedia.org/w/api.php?action=query'

        r = self.geosearch()
        p_id = self.find_page_id(r)
        self.get_content(p_id)

    def geosearch(self):
        coordinates = self._latitude + '|' + self._longitude
        params = { 'list' : 'geosearch',
                    'gsradius' : 10000,
                    'gscoord' : coordinates,
                    'gslimit' : 5,  # 5 first results
                    'format' : 'json',
                    'formatversion' : 2 # UTF8
                    }
        response = requests.get(url=self._url, params=params)

        if response.status_code == requests.codes.ok:
            response = response.json()
        else:
            response = response.raise_for_status()
        return response

    def find_page_id(self, response):
        page_id = 0
        ind = 0
        for _ in response["query"]["geosearch"]:
            if response["query"]["geosearch"][ind]["title"] == self._title:
                page_id = response["query"]["geosearch"][ind]["pageid"]
            ind += 1
        return page_id

    def get_content(self, p_id):
        params = { "pageids" : p_id,
                   "prop" : "extracts",
                   "exintro" : 1, # intro
                   "explaintext" : "",# remove html content
                   "format" : "json",
                   "formatversion" : 2}
        resp = requests.get(self._url, params=params)

        if resp.status_code == requests.codes.ok:
            resp = resp.json()
            resp = resp["query"]["pages"][0]["extract"]
        else:
            resp = resp.raise_for_status()
        return resp


# w = WikiMedia(48.8747578, 2.350564700000001, "Cité Paradis")
