from flask import Flask
from flask import request
from app import app
from app.models.city import City
from app.models.base import db
from flask import jsonify
from flask import make_response
import md5
import json


@app.route('/states/<state_id>/cities', methods=['GET','POST'])

def list_cities(state_id):
    id_state = state_id
    #returns a json with the cities associated to a state
    if request.method == 'GET':
        list =[]
        for city in City.select().where(City.state == id_state):
            list.append(city.name)
            j = json.dumps(list)
            parsed = json.loads(j)
        return jsonify(parsed)
    #creates a new city
    if request.method == 'POST':
        city_name = request.form['name']
        new_city = City(name=request.form['name'], state_id=id_state)
        new_city.save()
        return "New city saved\n"
