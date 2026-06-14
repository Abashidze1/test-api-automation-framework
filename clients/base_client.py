import requests

from utils.logger import logger


class BaseClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.session = requests.Session()

    def _log_request(self, method, url, json=None, params=None):
        logger.info(f"REQUEST: {method} {url}")
        if params:
            logger.info(f"PARAMS: {params}")
        if json:
            logger.info(f"REQUEST BODY: {json}")

    def _log_response(self, response):
        logger.info(f"STATUS CODE: {response.status_code}")
        logger.info(f"RESPONSE BODY: {response.text}")

    def get(self, endpoint, params=None):
        url = self.BASE_URL + endpoint
        self._log_request("GET", url, params=params)
        response = self.session.get(url, params=params)
        self._log_response(response)
        return response

    def post(self, endpoint, json=None):
        url = self.BASE_URL + endpoint
        self._log_request("POST", url, json=json)
        response = self.session.post(url, json=json)
        self._log_response(response)
        return response

    def put(self, endpoint, json=None):
        url = self.BASE_URL + endpoint
        self._log_request("PUT", url, json=json)
        response = self.session.put(url, json=json)
        self._log_response(response)
        return response

    def patch(self, endpoint, json=None):
        url = self.BASE_URL + endpoint
        self._log_request("PATCH", url, json=json)
        response = self.session.patch(url, json=json)
        self._log_response(response)
        return response

    def delete(self, endpoint):
        url = self.BASE_URL + endpoint
        self._log_request("DELETE", url)
        response = self.session.delete(url)
        self._log_response(response)
        return response