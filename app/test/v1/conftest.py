import pytest
from app import create_app


@pytest.fixture
def app():

    ''' initialize test to testing mode '''
    app = create_app({
        'TESTING': True
    })

    yield app


@pytest.fixture
def client(app):
    return app.test_client()
