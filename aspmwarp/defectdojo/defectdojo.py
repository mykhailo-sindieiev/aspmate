import json

import requests
from urllib.parse import urljoin

class DefectDojo:
    def __init__(self, url, key):
        self.url = url
        self.key = key
        self.headers = {'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'Authorization': 'Token ' + self.key}
        self.session = requests.Session()
        self.session.headers.update(self.headers)

        # API endpoints
        self.PRODUCTS_API = '/api/v2/products/'


    def close(self):
        self.session.close()

    @staticmethod
    def _get_kwargs(key, dictionary):
        if key in dictionary:
            return dictionary[key]
        else:
            return None

    def create_product(self, name: str, description: str, prod_type: int, **kwargs) -> int:
        """
        Create a new product in the DefectDojo

        :param name: Name of the product to create
        :param description:
        :param prod_type: Product type. Should be the integer and should match the product type ID
        :return: Status code, answer in json format
        """

        data = {"name": name, "prod_type": prod_type, "description": description}
        payload = data | kwargs.get("additional_fields")

        print(payload)
        create_url = urljoin(self.url, self.PRODUCTS_API)
        resp = self.session.post(url=create_url, json=data)
        return resp.status_code
