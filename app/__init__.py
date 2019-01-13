import os
from flask import Flask, jsonify, make_response
from flask import json
from flask_jwt_extended import JWTManager
from instance.config import app_config
from .api.v1.views.meetup import meetup
from .api.v1.views.auth import auth
from .api.v1.views.questions import question


def create_app(config_name):
    # initialize the app and configures it
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config)
    app.config.from_pyfile('config.py')
    app.config['JWT_SECRET_KEY'] = 'yjfhrtht'
    jwt = JWTManager(app)

    '''registers the blueprints'''

    app.register_blueprint(auth)
    app.register_blueprint(meetup)
    app.register_blueprint(question)

    # factory set app
    @app.route('/')
    def hello():
        return make_response(jsonify({"message": "hello, world!"})), 200
    return app
