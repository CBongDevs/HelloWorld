from flask import Flask
from .controllers import ping


def create_app(app):
    app.register_blueprint(ping.controller, url_prefix='/api/v1')
