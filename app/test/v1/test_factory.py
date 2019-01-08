from app import create_app
from flask import json
from instance.config import app_config


def test_config():
    assert not create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get(
            '/hello',
            data=json.dumps({'message': 'hello, world!'}),
            content_type='application/json'
        )
    assert response