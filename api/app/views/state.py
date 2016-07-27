from flask import make_response
from flask import request
from app import app
from app.models.base import db
from app.models.state import State
from flask_json import jsonify


@app.route('/states', methods=['GET', 'POST'])
def list_of_states():
    if request.method == 'GET':
        list = []
        for state in State.select():
            list.append(state.to_hash())
        return jsonify(list)

    if request.method == 'POST':
        # name_state = request.form['name']
        try:
            new_state = State(name=request.form['name'])
            # saving the changes
            new_state.save()
            # returning the new information in hash form
            return "New State entered! -> %s\n" % (new_state.name)
        except:
            return make_response(jsonify({'code': 10000, 'msg': 'State already exist'}), 409)


@app.route('/states/<state_id>', methods=['GET', 'DELETE'])
def modify_state(state_id):
    try:
        # displaying state by id
        if request.method == 'GET':
            id = state_id
            return jsonify(State.get(State.id == id).to_hash())
    except:
        return "No State was found with id %d\n" % (int(id))
    if request.method == 'DELETE':
        id = state_id
        try:
            # creating and oobject calling the State
            get_state = State.get(State.id == id)
            # deleting state based on the id
            get_state.delete_instance()
            return "State with id %d was deleted\n" % (int(id))
        except:
            return "No State was found with id %d\n" % (int(id))
