import pytest
from flask import json


class Setup_question():
    # setups the tests
    def __init__(self, client, headers):
        self._client = client
        self._headers = headers

    def Create_question(self, user=2,
                        meetup=1,
                        title='flask',
                        body='There available by injected humour, or randomised words which don\'t look even slightly believable?'
                        ):
        return self._client.post(
            '/api/v1/question/',
            data=json.dumps({'user': user,
                             'meetup': meetup,
                             'title': title,
                             'body': body,
                             }),
            content_type='application/json', headers=self._headers
        )

    def vote(self, url):
        return self._client.patch(
            url,
            content_type='application/json', headers=self._headers
        )


# creates a fixture for class questions
@pytest.fixture
def questions(client, headers):
    return Setup_question(client, headers)


def test_create_question(questions):
    response = questions.Create_question()

    assert response.status_code == 201


def test_voteup(questions):
    response = questions.vote('/api/v1/question/upvote/1')

    assert response.status_code == 200


def test_votedown(questions):
    response = questions.vote('/api/v1/question/downvote/1')

    assert response.status_code == 200


def test_fail_votedown(questions):
    response = questions.vote('/api/v1/question/downvote/5')

    assert response.status_code == 404


def test_fail_voteup(questions):
    response = questions.vote('/api/v1/question/upvote/5')

    assert response.status_code == 404
