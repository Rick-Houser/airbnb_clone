from flask_json import FlaskJSON, json_response
from flask import make_response
from datetime import datetime
from flask import jsonify
from app import app, models
import peewee

'''
  Handle GET requests
    - index: return current date and time from utc and server
    - before_request: establish database connection
    - after_request: close database connection
'''


@app.route('/', methods=['GET'])
def index():
    return json_response(status='OK',
                         utc_time=datetime.utcnow().strftime('%d/%m/%Y %H:%M:%S'),
                         time=datetime.now().strftime('%d/%m/%Y %H:%M:%S'))


def before_request():
    peewee.models.database.connect()


def after_request():
    peewee.models.database.close()


@app.errorhandler(404)
# Error handling
def not_found(error):
    return make_response(jsonify({'code': '404', 'msg': 'not found'}), 404)
