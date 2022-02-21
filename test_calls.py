from dotenv import dotenv_values

from news_api_calls import send_request

config = dotenv_values(".env")
import pytest


class TestCalls:
    def test_send_request(self):
        payload = {'apiKey': config.get('NEWS_API_KEY'),
                   }
        response = send_request(f"{config.get('URL')}/v2/sources", payload)
        assert response.get('status') == 'ok'

    def test_send_request_without_config(self):
        payload = {'apiKey': None,
                   }
        response = send_request(f"{config.get('URL')}/v2/sources", payload)
        assert not response

    def test_call_function_without_args(self):
        with pytest.raises(TypeError):
            send_request()
