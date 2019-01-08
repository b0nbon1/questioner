from flask import Flask, jsonify, make_response
from instance.config import app_config
from flask import json


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config)
    app.config.from_pyfile('config.py')

    # factory set app
    @app.route('/hello')
    def hello():
        return make_response(jsonify({"message": "hello, world!"})), 200

    return app
