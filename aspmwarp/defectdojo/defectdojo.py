import requests
from urllib.parse import urljoin

class DefectDojo:
    def __init__(self, url, key):
        self.url = url
        self.key = key
        self.headers = {'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'Authorization': 'Bearer ' + key}
        self.session = requests.Session()
        self.session.headers.update(self.headers)

        # API endpoints
        self.CREATE_PRODUCT_API = '/'
        self.DELETE_PRODUCT_API = '/products/'


    def close(self):
        self.session.close()

    def create_product(self, name: str) -> int:
        """
        Create a new product in the DefectDojo

        :param name: name of the product to create
        :return: status code, answer in json format
        """
        create_url = urljoin(self.url, self.CREATE_PRODUCT_API)
        resp = self.session.post(url=create_url, json={'name': name})

