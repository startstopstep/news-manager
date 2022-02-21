import csv
import logging
from datetime import datetime
import boto3
from dotenv import dotenv_values
from news_api_calls import send_request
from utils import *

# .env file should have 4 constant variables:
# URL - website url, in our case: https://newsapi.org/
# NEWS_API_KEY - personal API key for NewsAPI
# ACCES_KEY_ID - personal ACCES KEY ID for AWS S3
# SECRET_ACCES_KEY - personal SECRET ACCES KEY for AWS S3
config = dotenv_values('.env')


class NewsAPI:
    def __call__(self):
        sources = self.get_sources()
        top_headlines = self.get_topheadlines(sources)
        file_name = self.save_topheadlines(top_headlines)
        self.upload_topheadlines(file_name)

    def get_sources(self) -> list:
        payload = {'apiKey': config.get('NEWS_API_KEY'),
                   'language': 'en',
                   }

        response = send_request(f"{config.get('URL')}/v2/sources", payload)

        if not response:
            raise ThirdPartyError(ThirdPartyError.message)

        sources = list()
        for i in range(len(response['sources'])):
            sources.append(response['sources'][i]['name'])
        return sources

    def get_topheadlines(self, sources: list) -> list:
        if not isinstance(sources, list):
            logging.error(IncorrectArgType.message)
            raise IncorrectArgType(IncorrectArgType.message)
        src = ','.join(sources)
        payload = {'apiKey': config.get('NEWS_API_KEY'),
                   'language': 'en',
                   'sources': src,
                   'pageSize': "100",
                   }

        response = send_request(f'{config.get("URL")}/v2/top-headlines', payload)
        if not response:
            raise ThirdPartyError(ThirdPartyError.message)

        top_headlines = [['name', 'author', 'title'], ]
        for i in range(len(response['articles'])):
            top_headlines.append([
                response['articles'][i]['source']['name'],
                response['articles'][i]['author'],
                response['articles'][i]['title']
            ])
        return top_headlines

    def save_topheadlines(self, top_headlines: list) -> str:
        if not isinstance(top_headlines, list):
            logging.error(IncorrectArgType.message)
            raise IncorrectArgType(IncorrectArgType.message)
        self.file_name = f'{datetime.now().strftime("%d.%m.%Y_%H:%M:%S")}_headlines.csv'

        with open(self.file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(top_headlines)

        return self.file_name

    def upload_topheadlines(self, file_name: str) -> None:
        if not isinstance(file_name, str):
            logging.error(IncorrectArgType.message)
            raise IncorrectArgType(IncorrectArgType.message)

        try:
            session = boto3.Session(
                aws_access_key_id=config.get('ACCES_KEY_ID'),
                aws_secret_access_key=config.get('SECRET_ACCES_KEY'),
            )

            s3 = session.resource('s3')
            s3.Bucket('newssources').upload_file(file_name, file_name)
        except boto3.exceptions.S3UploadFailedError:
            logging.error(InvalidAwsKey.message)
            raise InvalidAwsKey()


if __name__ == '__main__':
    NewsAPI()()
