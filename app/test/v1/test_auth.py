import pytest
from flask import json


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def register(self, firstname='test1',
                 lastname='test2',
                 othername='test3',
                 PhoneNumber='254712345678',
                 email='test1@test.com',
                 username='pytest',
                 password='testpytest',
                 confirm_password='testpytest'):
        return self._client.post(
            '/api/v1/auth/register',
            data=json.dumps({'firstname': firstname,
                             'lastname': lastname,
                             'othername': othername,
                             'PhoneNumber': PhoneNumber,
                             'email': email,
                             'username': username,
                             'password': password,
                             'confirm_password': confirm_password}),
            content_type='application/json'
        )


@pytest.fixture
def auth(client):
    return AuthActions(client)


def test_register(client, auth):
    response = auth.register()
    assert response.status_code == 200
