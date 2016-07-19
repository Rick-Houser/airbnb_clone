from flask_json import FlaskJSON, json_response
from flask import make_response
from datetime import datetime
from flask import jsonify
from app import app, models
import peewee


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
def not_found(error):
    return make_response(jsonify({'code': '404', 'msg': 'not found'}), 404)
    # json_response(code='404', msg='Not found')
    # make_response(jsonify({'code':'404', 'msg':'not found'}),404)
