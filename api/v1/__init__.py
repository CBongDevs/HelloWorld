from flask import Flask
from .controllers import ping
from .models import db
from .models import user

def create_app(app):
    app.register_blueprint(ping.controller, url_prefix='/api/v1')
    db.init_app(app)