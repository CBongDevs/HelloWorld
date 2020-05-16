from os import getenv
from flask import Flask
from flask_migrate import Migrate

from api.config import Config
from api.models import db
from api.v1 import create_app as create_app_v1
from api.v2 import create_app as create_app_v2


def create_app():
    app = Flask(__name__, static_folder='./web/build', static_url_path='/')
    app.config.from_object(Config)
    with app.app_context():
        db.init_app(app)
        
        migrate = Migrate(app, db, directory='api/migrations')

        create_app_v1(app)
        create_app_v2(app)

        @app.route('/')
        def index():
            return app.send_static_file('index.html')
        
        return app


# gunicorn looks for `application` by default
application = create_app()