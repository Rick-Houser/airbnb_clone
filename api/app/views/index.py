from flask import Flask
from flask_json import FlaskJSON, json_response
from datetime import datetime
from app import app, models
import peewee


@app.route('/', methods=['GET'])
def index():
    return json_response(status = 'OK',
                utc_time = datetime.utcnow().strftime('%Y/%m/%d %H:%M:%S'),
                time = datetime.now().strftime('%Y/%m/%d %H:%M:%S'))

def before_request():
    peewee.models.database.connect()

def after_request():
    peewee.models.database.close()

@app.errorhandler(404)
def not_found(e):
    return json_response(code='404', msg='Not found')
