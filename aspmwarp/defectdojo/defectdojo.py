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


    def create_product(self, name: str, description: str, prod_type: int, **kwargs):
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

        if resp.status_code != 201:
            prod_id = self.get_product_name_exact(name=name)
        else:
            prod_id = resp.json()["id"]

        return prod_id


    def get_product_name_exact(self, name: str):
        """
        Returns the product id of the product with the given name

        :param name: Name of the product to get
        :return: DefectDojo product id
        """
        search_exact_url = f"{self.url}{self.PRODUCTS_API}?name_exact={name}"
        resp = self.session.get(url=search_exact_url)

        # I am hardcoding here to fetch the first element
        # because DefectDojo does not allow to create 2 product with the same name
        prod_id = resp.json().get("results")[0].get("id")

        return prod_id


    def delete_product(self, product_id: int):
        """
        Delete a product from the DefectDojo by id

        :param product_id: ID of the product to delete
        :return: status code, answer in json format
        """
        delete_url = urljoin(self.url, self.PRODUCTS_API + str(product_id))

        resp = self.session.delete(url=delete_url)

        return resp.status_code
