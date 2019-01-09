from flask import Flask, jsonify, make_response
from instance.config import app_config
from flask import json


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config)
    app.config.from_pyfile('config.py')

    from .api.v1.views.auth import auth
    app.register_blueprint(auth)

    from .api.v1.views.meetup import meetup
    app.register_blueprint(meetup)

    from .api.v1.views.questions import question
    app.register_blueprint(question)

    # factory set app
    @app.route('/hello')
    def hello():
        return make_response(jsonify({"message": "hello, world!"})), 200

    return app
