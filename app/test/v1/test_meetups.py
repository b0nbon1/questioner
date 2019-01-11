import pytest
from flask import json


class Setup_meetup():
    # setups the tests
    def __init__(self, client, headers):
        self._client = client
        self._headers = headers

    def Create_meetup(self, topic='Flask', location='Nairobi',
                      happeningOn='1st Feb',
                      images=['https://www.cs.ucdavis.edu/wp-content/uploads/2014/02/cover.jpg',
                              'https://www.gsd.harvard.edu/wp-content/uploads/2017/08/Lib-Lab.jpg'],
                      tags=['python', 'flask']):
        return self._client.post(
            '/api/v1/meetup/',
            data=json.dumps({'topic': topic,
                             'location': location,
                             'happeningOn': happeningOn,
                             'images': images,
                             'tags': tags}),
            content_type='application/json', headers=self._headers
        )

    def rsvp(self, url, status):
        return self._client.post(
            url,
            data=json.dumps({
                'status': status
            }),
            content_type='application/json', headers=self._headers
        )


# creates fixture meetup
@pytest.fixture
def meetups(client, headers):
    return Setup_meetup(client, headers)


def test_create_meetup(meetups):
    response = meetups.Create_meetup()

    assert response.status_code == 201


def test_get_all_meetups(client, headers):
    assert client.get('/api/v1/meetup/upcoming', headers=headers).status_code == 200


def test_get_specific_meetup(client, headers):
    assert client.get('/api/v1/meetup/1', headers=headers).status_code == 200


def test_get_specific_meetup_not_found(client, headers):
    assert client.get('/api/v1/meetup/4', headers=headers).status_code == 404


def test_delete_meetup(client, headers):
    assert client.delete('/api/v1/meetup/1', headers=headers).status_code == 200


def test_delete_meetup_not_found(client, headers):
    assert client.delete('/api/v1/meetup/4', headers=headers).status_code == 404


def test_create_rsvp(meetups):
    response = meetups.rsvp('/api/v1/meetup/2/rsvps')

    assert response.status_code == 201


@pytest.mark.parametrize(('url', 'status', 'status_code'), (
    ('/api/v1/meetup/6/rsvps', 'yes', 404),
    ('/api/v1/meetup/2/rsvps', 'kgggiyt', 406),
    ('/api/v1/meetup/3/rsvps', 'yes', 201),
    ('/api/v1/meetup/3/rsvps', 'maybe', 201),
    ('/api/v1/meetup/3/rsvps', 'no', 201),
))
def test_create_rsvp(meetups, url, status, status_code):
    response = meetups.rsvp(url, status)
    assert response.status_code == status_code
