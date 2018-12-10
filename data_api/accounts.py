import requests
import logging
import json
import urllib3
import datetime

from settings.config import DATA_API

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logger = logging.getLogger(__name__)


class AccountsAPI(object):
    request_timeout = 25
    endpoint = DATA_API + 'accounts/'

    def __init__(self):
        self._s = requests.Session()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._s = None

    def account_transactions_json(self, address, start=None, end=None, type=None, result='tesSUCCESS', limit=1000, marker=None):
        url = self.endpoint + f'{address}/transactions?'

        if start is not None and end is not None:
            url += f'&start={start.strftime("%Y-%m-%dT%H:%M:%S")}&end={end.strftime("%Y-%m-%dT%H:%M:%S")}'

        if marker is not None:
            url += f'&marker={marker}'

        if type is not None:
            url += f'&type={type}'

        url += f'&result={result}&limit={limit}'

        logger.info(url)
        try:
            return self._s.get(url, verify=False, timeout=self.request_timeout).json()
        except Exception as e:
            logger.info(e)
