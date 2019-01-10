import pytest
from flask import json


class Setup_auth():
    # setups the tests
    def __init__(self, client):
        self._client = client

    def login(self, username='pytest2', password='test2guy'):
        return self._client.post(
            '/api/v1/auth/login',
            data=json.dumps({'username': username, 'password': password}),
            content_type='application/json'
        )

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


# creates a fixture for class auth
@pytest.fixture
def auth(client):
    return Setup_auth(client)


def test_login(client, auth):
    response = auth.login()

    assert response.status_code == 200


@pytest.mark.parametrize(('username', 'password', 'status_code'), (
    ('not', 'test', 404),
    ('pytest2', 'guess', 401),
    ('pytest2', 'test2guy', 200)
))
def test_login_validate_input(auth, username, password, status_code):
    response = auth.login(username, password)
    assert response.status_code == status_code


def test_register(client, auth):
    response = auth.register()
    assert response.status_code == 201
