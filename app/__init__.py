from flask import Flask
from config import config

APP_NAME = 'FLASK_CELERY'


def create_app(config_name):
    app = Flask(APP_NAME)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app
