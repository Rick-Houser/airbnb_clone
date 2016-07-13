from flask import Flask
from flask import request
from app import app
from app.models import user

@app.route('/users/',methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':

@app.route('/users/<user_id>/', methods=['GET','POST']):
