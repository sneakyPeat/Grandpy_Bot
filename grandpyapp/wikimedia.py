import requests


class WikiMedia:
    def __init__(self, latitude, longitude, title):
        self._latitude = str(latitude)
        self._longitude = str(longitude)
        self._title = title

        self._url = 'https://fr.wikipedia.org/w/api.php?action=query'

        r = self.geosearch()
        self._p_id = self.find_page_id(r)
        if self._p_id != 0:
            self._extract_json = self.extract_content(self._p_id)
            self._content = self.get_contents(self._extract_json)
        else:
            self._content = "nothing found"

    @property
    def title(self):
        return self._title

    @property
    def content(self):
        return self._content

    @property
    def page_id(self):
        return self._p_id

    def geosearch(self):
        coordinates = self._latitude + '|' + self._longitude
        params = {
            'list': 'geosearch',
            'gsradius': 10000,
            'gscoord': coordinates,
            'gslimit': 5,  # 5 first results
            'format': 'json',
            'formatversion': 2  # UTF8
        }
        response = requests.get(self._url, params=params)

        if response.status_code == requests.codes.ok:
            response = response.json()
        else:
            response = response.raise_for_status()
        return response

    def find_page_id(self, response):
        page_id = 0
        ind = 0

        if not response["query"]["geosearch"]:
            pass
        else:
            for _ in response["query"]["geosearch"]:
                if response["query"]["geosearch"][ind]["title"] == self._title:
                    page_id = response["query"]["geosearch"][ind]["pageid"]
                ind += 1

            # if query has not the same title, take the closest position
            if page_id == 0:
                page_id = response["query"]["geosearch"][0]["pageid"]
                self._title = response["query"]["geosearch"][0]["title"]
        return page_id

    def extract_content(self, p_id):
        params = {
            "pageids": p_id,
            "prop": "extracts",
            "exintro": 1,  # intro
            "explaintext": "",  # remove html content
            "format": "json",
            "formatversion": 2
        }
        resp = requests.get(self._url, params=params)

        if resp.status_code == requests.codes.ok:
            resp = resp.json()
        else:
            resp = resp.raise_for_status()
        return resp

    def get_contents(self, extracts_json):
        return extracts_json["query"]["pages"][0]["extract"]
