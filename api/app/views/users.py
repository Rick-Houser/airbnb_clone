from flask import Flask
from flask import request
from flask.views import View
from app import app
from app.models import user
from flask_json import json_response


@app.route('/users/',methods=['GET', 'POST'])
class user_list(View):
    #Getting a list of all users
    if request.status == 'GET':
        def dispatch_request(self):
            users = user.query.all()
            return json_response(users)
    #creating new users
    elif request.method == 'POST':
        def new_user():
            first_name = request.form['inputName']
            last_name =request.form['inputLastName']
            #need to validate email
            email = request.form['inputEmail']
            password = request.form['inputPassword']
