from flask import jsonify, request
from flask_json import json_response
from app.models.user import User
from app import app
from peewee import *
from flask import make_response
import md5


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        try:
            list = []
            for user in User.select():
                list.append(user.to_hash())
                return jsonify(list)
        except:
            return make_response(jsonify({'code': 10000,
                                          'msg': 'users not found'}), 404)

    elif request.method == 'POST':
        user_email = request.form["email"]
        user_password = request.form["password"]
        user_first_name = request.form["first_name"]
        user_last_name = request.form["last_name"]
        try:
            new_user = User(email=user_email,
                            first_name=user_first_name,
                            last_name=user_last_name,
                            password=md5.new(user_password).hexdigest())
            new_user.save()
            return jsonify(new_user.to_hash())
        except:
            return make_response(jsonify({'code': 10000,
                                          'msg': 'email already exist'}), 409)


@app.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def modify_users(user_id):
    if request.method == 'GET':
        try:
            id = user_id
            # returning a hash with the user information
            return jsonify(User.get(User.id == id).to_hash())
        except:
            return make_response(jsonify({'code': 10000,
                                          'msg': 'user not found'}), 404)

    elif request.method == 'PUT':
        id = user_id

        try:
            # selecting the user by its id
            # updating users first name
            query = User.update(first_name=request.form['first_name']).where(User.id == id)
            # added the folling line since it did not seem to do it at the end
            query.execute()
        except:
            pass

        try:
            # updating user last_name
            query = User.update(last_name=request.form['last_name']).where(User.id == id)
            query.execute()
        except:
            pass
        try:
            # updating and securing the password
            query = User.update(password=md5.new(request.form['password']).hexdigest()).where(User.id == id)
            query.execute()
        except:
            pass
            # returning message when trying to update email
        if request.form['email']:
            return make_response(jsonify({'code': 10000, 'msg': 'email can not be updateed'}), 409)
        query.execute()
        return "updated\n"

    if request.method == 'DELETE':
        id = user_id
        try:
            # creating an object
            get_user = User.get(User.id == id)
            # deleting the instance of the object
            get_user.delete_instance()
            return "User with id = %d was deleted\n" % (int(id))
        except:
            return "No user was found with id %d\n" % (int(id))
