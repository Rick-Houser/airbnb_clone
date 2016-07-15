from flask import Flask
from flask import request
from app import app
from app.models.place import Place
from app.models.base import db
from flask import jsonify
from flask import make_response
import md5
import json
from playhouse.shortcuts import model_to_dict

@app.route('/places', methods = ['GET', 'POST'])

def list_of_place():
    #returning a list of all places
    if request.method == 'GET':
        list = []
        for place in Place.select():
            list.append(place.name)
            j = json.dumps(list)
            parsed = json.loads()
        return jsonify(parsed)
    if request.method == 'POST':
        new_place = Place(owner=request.form['owner'],
                          city=request.form['city'],
                          name=request.form['name'],
                          description=request.form['description'],
                          number_rooms=request.form['number_rooms'],
                          number_bathrooms=request.form['number_bathrooms'],
                          max_guest=request.form['max_guest'],
                          price_by_night=request.form['price_by_night'],
                          latitude=request.form['latitude'],
                          longitude=request.form['longitude']
                         )
        new_place.save()
@app.route('/places/<place_id>', methods=['GET','PUT', 'DELETE'])
def modify_place(place_id):
    id = place_id
    if request.method == 'GET':
        return Place.get(Place.id == id).to_hash()

    if request.method == 'PUT':
        id = place_id
        try:
            #uptading name
            query = Place.update(name = request.form['name']).where(Place.id == id)
        except:
            pass
        try:
            #updating description
            query = Place.update(description = request.form['description']).where(Place.id == id)
        except:
            pass

        try:
            #updating user last_name
            query = Place.update(number_rooms = request.form['number_rooms']).where(Place.id == id)
        except:
            pass
        try:
            #updating and securing the password
            query = Place.update(number_bathrooms = request.form['number_bathrooms']).where(Place.id == id)
        except:
            pass
        try:
            query = Place.update(max_guest = request.form['max_guest']).where(Place.id == id)
        except:
            pass
        try:
            query = Place.update(price_by_night = request.form['price_by_night']).where(Place.id == id)
        except:
            pass
        try:

            query = Place.update(latitude = request.form['latitude']).where(Place.id == id)
        except:
            pass
        try:

            query = Place.update(longitude = request.form['longitude']).where(Place.id == id)
        except:
            pass
            #returning message when trying to update owner or email
        if request.form['owner']:
            return "Owner can not be updated\n"
        if request.form['city']:
            return "City can not be updated\n"
        query.execute()
        return "updated\n"

    if request.method == 'DELETE':
        try:
            get_place = Place.get(Place.id == id)
            get_place.delete_instance()
        except:
            return make_response(jsonify({'code':'10001', 'msg':'no place found with that id'}),409)
