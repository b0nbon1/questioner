from flask import Flask
from instance.config import app_config


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config)
    app.config.from_pyfile('config.py')

    from .api.v1.views.auth import auth
    app.register_blueprint(auth)

    # factory set app
    @app.route('/hello')
    def hello():
        return jsonify({"message": "hello, world"})

    return app
