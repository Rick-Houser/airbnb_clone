from flask import Flask
from flask import request
from app import app
from app.models.user import User
from app.models.base import db
from flask import jsonify
from flask import make_response

@app.route('/users',methods=['GET', 'POST'])

def list_of_users():
    if request.method == 'GET':
        j = []
        for user in User.select():
            j.append(user.first_name)
        return jsonify(j)

    if request.method == 'POST':
        #stores the email comming from the post request
        email_tmp = request.form['email']
        #traverses the data base
        for user in User.select():
            #comparing each email in the data base against the post email
            if user.email == email_tmp:
                #returning error message and changing http header status code to 409
                return make_response(jsonify({'code':'10000','msg':'email already exist'}),409)

        new_user =User(first_name=request.form['first_name'],
                        last_name=request.form['last_name'],
                        #need to validate email
                        email=request.form['email'],
                        password=request.form['password'])

        new_user.save()
        return new_user.to_hash()


#class user_list(View):
    #Getting a list of all users
#    if request.status == 'GET':
#        def dispatch_request(self):
#            users = user.query.all()
#            return json_response(users)
#    #creating new users
#    elif request.method == 'POST':
#        def new_user():
#            first_name = request.form['inputName']
#            last_name =request.form['inputLastName']
#            #need to validate email
#            email = request.form['inputEmail']
#            password = request.form['inputPassword']
