import pytest
from flask import json


class Setup_meetup():
    def __init__(self, client):
        self._client = client

    def Create_meetup(self, topic='Flask', location='Nairobi',
                      happeningOn='1st Feb',
                      images=['https://www.cs.ucdavis.edu/wp-content/uploads/2014/02/cover.jpg',
                              'https://www.gsd.harvard.edu/wp-content/uploads/2017/08/Lib-Lab.jpg'],
                      tags=['python', 'flask']):
        return self._client.post(
            '/api/v1/meetup/create',
            data=json.dumps({'topic': topic,
                             'location': location,
                             'happeningOn': happeningOn,
                             'images': images,
                             'tags': tags}),
            content_type='application/json'
        )


@pytest.fixture
def meetups(client):
    return Setup_meetup(client)


def test_create_meetup(client, meetups):
    response = meetups.Create_meetup()

    assert response.status_code == 201


def test_get_all_meetups(client):
    assert client.get('/api/v1/meetup/upcoming').status_code == 200


def test_get_specific_meetup(client):
    assert client.get('/api/v1/meetup/1').status_code == 200


def test_fail_get_specific_meetup(client):
    assert client.get('/api/v1/meetup/4').status_code == 404
