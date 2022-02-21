import csv
import os
from unittest import TestCase
from unittest.mock import patch

import boto3

from data import *
from main import NewsAPI
from news_api_calls import send_request
from utils import *


class TestNewsManager(TestCase):
    @patch('main.send_request', return_value=sources_response_successful)
    def test_get_sources_succesful(self, mock_send_request):
        api = NewsAPI()
        sources = api.get_sources()
        self.assertEqual(sources, ['ABC News', 'ABC News (AU)'])

    @patch('main.send_request', return_value=False)
    def test_get_sources_error(self, mock_send_request):
        api = NewsAPI()
        with self.assertRaises(ThirdPartyError):
            api.get_sources()

    @patch('main.send_request', return_value=top_headlines_response_successful)
    def test_get_topheadlines_successful(self, mock_send_request):
        api = NewsAPI()
        top_headlines = api.get_topheadlines(['ABC News', 'ABC News (AU)'])
        self.assertEqual(top_headlines, top_headlines_result_successful)

    @patch('main.send_request', return_value=False)
    def test_get_topheadlines_error(self, mock_send_request):
        api = NewsAPI()
        with self.assertRaises(ThirdPartyError):
            api.get_topheadlines(['ABC News', 'ABC News (AU)'])

    def test_save_topheadlines_to_file(self):
        api = NewsAPI()
        api.save_topheadlines(top_headlines_result_successful)
        headlines_result = api.file_name
        headlines_example = 'example.csv'

        with open(headlines_example, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(top_headlines_result_successful)

        with open(headlines_result, 'r') as t1, open(headlines_example, 'r') as t2:
            fileone = t1.readlines()
            filetwo = t2.readlines()
            self.assertEqual(fileone, filetwo)

        os.remove(headlines_result)
        os.remove(headlines_example)

    def test_input_incorrect_args(self):
        api = NewsAPI()
        with self.assertRaises(IncorrectArgType):
            api.get_topheadlines("Test string")
        with self.assertRaises(IncorrectArgType):
            api.save_topheadlines("Test string")
        with self.assertRaises(IncorrectArgType):
            api.upload_topheadlines(["1", "2"])
        with self.assertRaises(IncorrectArgType):
            send_request(1, 2)

    @patch('main.boto3.Session', side_effect=boto3.exceptions.S3UploadFailedError)
    def test_upload_topheadlines_exception(self, mock_boto3):
        api = NewsAPI()
        headlines_example = 'example.csv'
        with open(headlines_example, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(top_headlines_result_successful)

        with self.assertRaises(InvalidAwsKey):
            api.upload_topheadlines(headlines_example)

        os.remove(headlines_example)
