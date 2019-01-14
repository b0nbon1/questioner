import json


# tests the factory
def test_hello(client):
    message = b"hello, world!"
    response = client.get('/')
    assert message in response.data
