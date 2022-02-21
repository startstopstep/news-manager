import logging

import requests
from dotenv import dotenv_values

from utils import *

config = dotenv_values(".env")


def send_request(url: str, payload: dict):
    if not (isinstance(url, str) or isinstance(payload, dict)):
        logging.error(IncorrectArgType.message)
        raise IncorrectArgType(IncorrectArgType.message)
    response = requests.get(url, params=payload).json()
    if response.get('status') == 'ok':
        return response
    else:
        error = response.get('code')
        error_message = response.get('message')
        logging.error(f'{error}: {error_message}')
        return False
