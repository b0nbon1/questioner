import pytest
from flask import json


class Setup_auth():
    # setups the tests
    def __init__(self, client):
        self._client = client

    def login(self, username='pytest2', password='testpytest1'):
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
                 username='pytest3',
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
    ('pytest2', 'testpytest1', 200)
))
def test_login_validate_input(auth, username, password, status_code):
    response = auth.login(username, password)
    assert response.status_code == status_code


def test_register(client, auth):
    response = auth.register()
    assert response.status_code == 201


@pytest.mark.parametrize(("username", "email", "password", "confirm_password", "error"), [
    ("te", "testguuk@test.com", "testpytest", "testpytest", b"invalid username"),
    ("test2", "test", "testpytest", "testpytest", b"invalid email"),
    ("test3", "test@test.com", "test", "test", b"invalid password"),
    ("pytest2", "testrtrty@test.com", "testpytest", "testpytest", b"username exists"),
    ("test4", "test1@login.com", "testpytest", "testpytest", b"email exists"),
    ("test4", "test@test.com", "testpytest", "test", b"Passwords don't match"),
])
def test_register_validate_input(auth, username, email, password, confirm_password, error):
    response = auth.register(firstname='test1', lastname='test2', othername='test3',
                             PhoneNumber='873462', username=username, email=email,
                             password=password, confirm_password=confirm_password)

    assert error in response.data


def test_empty_fiels(auth):
    response = auth.register(firstname='', lastname='', othername='',
                             PhoneNumber='', username='', email='',
                             password='', confirm_password='')

    assert b'all fields required' in response.data
