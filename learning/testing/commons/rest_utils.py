__author__ = 'arobres'


# Standard library imports
import logging
from json import JSONEncoder

# imports 3rd party libs
import requests
from requests.auth import HTTPBasicAuth

APP_IP = u'127.0.0.1'
APP_PORT = u'8000'
HEADERS = {'content-type': 'application/json'}

SERVER = 'http://127.0.0.1:8000'
QUESTIONS_PATTERN = '{url_root}/questions/'
QUESTION_DETAIL_PATTERN = '{url_root}/questions/{question_id}'
USER_DETAIL_PATTERN = '{url_root}/user/{user_id}'
PLAY_PATTERN = '{url_root}/play/'


class Rest_Utils(object):

    def __init__(self, username='qa', password='qa'):
        """Initialization method
        :param domain_id: ID of the BE domain calling Sprayer
        """
        self.username = username
        self.password = password
        self.api_url = SERVER
        self.encoder = JSONEncoder()

    def _call_api(self, pattern, method='post', body=None, headers=HEADERS, payload=None,
                  **kwargs):
        """Launch HTTP request against Sprayer API with given arguments
        :param pattern: string pattern of API url with keyword arguments (format string syntax)
        :param method: HTTP method to execute
        :param body: dictionary with JSON body content
        :param **kwargs: url parameters (without url_root or domain_id) to fill url pattern
        :returns: REST API response Json body (dict)
        """
        kwargs['url_root'] = self.api_url

        url = pattern.format(**kwargs)

        try:
            r = requests.request(method=method, url=url, data=self.encoder.encode(body), headers=headers,
                                 params=payload, auth=(self.username, self.password))
        except Exception, e:
            return None
        return r

    def create_one_question(self, body=None, headers=HEADERS):

        return self._call_api(QUESTIONS_PATTERN, method="post", body=body, headers=headers)

    def get_question_details(self, headers=None, question_id=None):

        return self._call_api(QUESTION_DETAIL_PATTERN, method="get", headers=headers, question_id=question_id)

    def get_random_question(self, headers=HEADERS):

        return self._call_api(QUESTIONS_PATTERN, method="get", headers=headers, payload='random')

    def get_user(self, headers=HEADERS, user_id=None):

        return self._call_api(USER_DETAIL_PATTERN, method='get', headers=headers, user_id=user_id)

    def get_question_play(self, headers=HEADERS):

        return self._call_api(PLAY_PATTERN, method='get', headers=headers)

    def send_answer(self, headers=HEADERS, body=None):

        return self._call_api(PLAY_PATTERN, method='post', headers=headers, body=body)