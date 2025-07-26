import requests

class DefectDojo:
    def __init__(self, url, key):
        self.url = url
        self.key = key
        self.headers = {'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'Authorization': 'Bearer ' + key}
        self.session = requests.Session()
        self.session.headers.update(self.headers)


    def close(self):
        self.session.close()
