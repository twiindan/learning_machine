__author__ = 'arobres'

from nose.tools import assert_true, assert_equals
from commons.rest_utils import Rest_Utils
import read_csv


api_utils = Rest_Utils()
'''
def test_create_one_question():

    response = api_utils.create_one_question(body={'question': 'test', 'answer': 'test1'})
    assert_true(response.ok, response.content)
    body_response = response.json()
    question_id = body_response['id']
    assert_equals(body_response['question'], 'test')
    assert_equals(body_response['answer'], 'test1')
    response = api_utils.get_question_details(question_id=question_id)
    body_response = response.json()
    assert_equals(body_response['question'], 'test')
    assert_equals(body_response['answer'], 'test1')


def test_get_random_question():

    response = api_utils.get_random_question()
    assert_true(response.ok, response.content)
    body_response = response.json()
    assert_equals(body_response['question'], 'test')
    assert_equals(body_response['answer'], 'test1')

'''


def test_to_populate_questions():

    all_countries = read_csv.obtain_all_countries()
    for country in all_countries:
        response = api_utils.create_one_question(body=country)
        assert_true(response.ok, response.content)
