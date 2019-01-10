import pytest
from app import create_app


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
