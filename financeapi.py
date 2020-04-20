from flask import Flask, render_template
from datetime import datetime
import os

app = Flask(__name__, static_folder='./finance-web/build', static_url_path='/')

@app.route('/api/ping')
def current_time():
    return { 'time': datetime.now(), 'env': os.getenv("FLASK_ENV") }

@app.route('/')
def index():
    return app.send_static_file('index.html')
