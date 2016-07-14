from flask import Flask
from flask import request
from app import app
from app.models.user import User
from app.models.base import db
from flask import jsonify
from flask import make_response
import md5
import json
from playhouse.shortcuts import model_to_dict, dict_to_model

@app.route('/users',methods=['GET', 'POST'])

def list_of_users():
    if request.method == 'GET':
        list = []
        for user in User.select():
            list.append(model_to_dict(user, exclude=[User.create_at, User.updated_at,User.password,User.is_admin]))
            j = json.dumps(list)
            parsed = json.loads(j)
        return json.dumps(parsed, indent=4, sort_keys=True)

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
                        email=request.form['email'],
                        password=md5.new(request.form['password']).hexdigest())

        new_user.save()
        return new_user.to_hash()


@app.route('/users/<user_id>',methods=['GET', 'PUT', 'DELETE'])
def modify_users(user_id):
    if request.method == 'GET':
        id = user_id
        #returning a hash with the user information
        return User.get(User.id == id).to_hash()

    if request.method == 'PUT':
        id = user_id

        try:
            #selecting the user by its id
            #updating users first name
            query = User.update(first_name = request.form['first_name']).where(User.id == id)
        except:
            pass

        try:
            #updating user last_name
            query = User.update(last_name = request.form['last_name']).where(User.id == id)
        except:
            pass
        try:
            #updating and securing the password
            query = User.update(password = md5.new(request.form['password']).hexdigest()).where(User.id == id)
        except:
            pass
            #returning message when trying to update email
        if request.form['email']:
            return "Email can not be updated\n"
        query.execute()
        return "updated\n"


    if request.method == 'DELETE':
        id = user_id
        try:
            #creating an object
            get_user = User.get(User.id == id)
            #deleting the instance of the object
            get_user.delete_instance()
            return "User with id = %d was deleted\n" %(int(id))
        except:
            return "No user was found with id %d\n" %(int(id))
