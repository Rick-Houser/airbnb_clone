from flask import Flask
from flask import request
from app import app
from app.models.city import City
from app.models.base import db
from flask import jsonify
from flask import make_response


@app.route('/states/<state_id>/cities', methods=['GET', 'POST'])
def list_cities(state_id):
    id_state = state_id
    # returns a json with the cities associated to a state
    if request.method == 'GET':
        list = []
        for city in City.select().where(City.state == id_state):
            list.append(city.to_dict())
        return jsonify(list)
    # creates a new city
    elif request.method == 'POST':
        # checks if the city already exist in the state
        for city in City.select():
            if str(city.state_id) == id_state and city.name == request.form['name']:
                return make_response(jsonify({'code': '10001',
                                              'msg': 'City already exists in this state'}), 409)

        city_name = request.form['name']
        new_city = City(name=city_name, state_id=id_state)
        new_city.save()
        return "New city saved %s\n" % (new_city)


@app.route('/states/<state_id>/cities/<city_id>', methods=['GET', 'DELETE'])
def modify_city(state_id, city_id):
    id = city_id
    try:
        if request.method == 'GET':
            list = []
            for city in City.select().where(City.id == id):
                list.append(city.to_dict())
            return jsonify(list)
    except:
        return "City with id %d does not exist" % (int(id))
    if request.method == "DELETE":
        id = city_id
        try:
            get_city = City.get(City.id == id)
            get_city.delete_instance()
            return "City with id %d was deleted\n" % (int(id))
        except:
            return "City with id %d does not exist\n" % (int(id))
