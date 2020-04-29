from datetime import datetime
from flask import Flask
from flask_restful import Resource

class Ping(Resource):
    def get(self):
        return { 
            'time': str(datetime.now())
        }