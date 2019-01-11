import pytest
from app import create_app
from flask_jwt_extended import create_access_token


@pytest.fixture
def app():

    ''' initialize test module to testing mode '''
    app = create_app({
        'TESTING': True,
    })

    yield app


# creates client fixture for app.test_client
@pytest.fixture
def client(app):
    return app.test_client()


# creates a jwt header for test authentications
@pytest.fixture
def headers(app):
    # enable the jwt to work in context within the app
    with app.app_context():
        access_token = create_access_token('hwfuqkeirhc4253redsf')
        headers = {'Authorization': 'Bearer {}'.format(access_token)}

    return headers
