from flask import Flask, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, static_folder='./build', static_url_path='/')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models.user import User

@app.route('/api/ping')
def current_time():
    return { 'time': datetime.now(), 'database_url': os.getenv('DATABASE_URL') }

@app.route('/')
def index():
    return app.send_static_file('index.html')
