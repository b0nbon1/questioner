import pytest
from flask import json


class Setup_question():
    def __init__(self, client):
        self._client = client

    def Create_question(self, user=2,
                        meetup=1,
                        title='flask',
                        body='There available by injected humour, or randomised words which don\'t look even slightly believable?'
                        ):
        return self._client.post(
            '/api/v1/question/new_question',
            data=json.dumps({'user': user,
                             'meetup': meetup,
                             'title': title,
                             'body': body,
                             }),
            content_type='application/json'
        )

    def vote(self):
        return self._client.patch(
            '/api/v1/question/upvote/1',
            content_type='application/json'
        )


@pytest.fixture
def questions(client):
    return Setup_question(client)


def test_login(client, questions):
    response = questions.Create_question()

    assert response.status_code == 201


def test_vote(client, questions):
    response = questions.vote()

    assert response.status_code == 200
