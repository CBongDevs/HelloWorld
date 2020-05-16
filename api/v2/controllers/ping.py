from os import getenv
from datetime import datetime
from flask import Flask
from flask_restful import Resource
from api.models import db

class Ping(Resource):
    def get(self):
        query = db.engine.execute('select * from public.alembic_version')
        revision = query.fetchone()['version_num']
        return { 
            'time': str(datetime.now()),
            'db' : {
                'revision' : revision
            },
            'database_url': getenv('DATABASE_URL')
        }
