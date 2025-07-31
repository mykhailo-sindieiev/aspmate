from typing import Any, Dict
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


    def create_product(self, name: str, description: str, prod_type: int, **kwargs) -> tuple[int, Dict[str, Any]]:
        """
        Create a new product in the DefectDojo

        :param name: Name of the product to create
        :param description: Description of the product to create
        :param prod_type: Product type. Should be the integer and should match the product type ID
        :param kwargs: Additional arguments that will be merged to the payload to DefectDojo
        :return: Status code, answer in json format
        """

        data = {"name": name, "prod_type": prod_type, "description": description}
        payload = data | kwargs.get("additional_fields")

        create_url = urljoin(self.url, self.PRODUCTS_API)
        resp = self.session.post(url=create_url, json=payload)

        return resp.status_code, resp.json()
