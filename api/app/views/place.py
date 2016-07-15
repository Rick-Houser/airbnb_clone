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
        list []
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
