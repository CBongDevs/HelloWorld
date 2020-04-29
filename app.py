from os import getenv
from flask import Flask
from datetime import datetime
from api.config import Config
from api.v1 import create_app as create_app_v1
from api.v2 import create_app as create_app_v2

# ------------------------------------------------------------------------------
# Importing a module twice (typically) does not execute the code a second time. 
# Why then is it important to `import models` from inside of the create_app d
# factory? Using a factory function instead of top level code means that the 
# app won't be created unless create_app is called, which prevents the full
# initialisation sequence from happening when you don't need it to. Note that
# on subsequent calls create_app will not return a fully initialised app.
def create_app():
    app = Flask(__name__, static_folder='./web/build', static_url_path='/')
    app.config.from_object(Config)
    with app.app_context():
        from api.v1.controllers import bad_route
        create_app_v1(app)
        create_app_v2(app)

        @app.route('/')
        def index():
            return app.send_static_file('index.html')
        
        return app
# gunicorn looks for `application` by default
application = create_app()