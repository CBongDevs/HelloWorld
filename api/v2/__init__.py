from flask import Flask
from flask_restful import Api
from .controllers import ping


def create_app(app: Flask):
    api = Api(app, prefix='/api/v2')
    api.add_resource(ping.Ping, '/ping')
