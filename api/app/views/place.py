from flask import Flask
from flask import request
from app import app
from app.models.place import Place
from app.models.base import db
from flask import jsonify
from flask import make_response


@app.route('/places', methods=['GET', 'POST'])
def list_of_place():
    # returning a list of all places
    if request.method == 'GET':
        list = []
        for place in Place.select():
            list.append(place.to_hash())
        return jsonify(list)

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
        return "place created"


@app.route('/places/<place_id>', methods=['GET', 'PUT', 'DELETE'])
def modify_place(place_id):
    id = place_id
    if request.method == 'GET':
        try:
            return jsonify(Place.get(Place.id == id).to_hash())
        except:
            return make_response(jsonify({'code': '10001',
                                          'msg': 'no place found'}), 404)
    elif request.method == 'PUT':
        place = Place.select().where(Place.id == place_id).get()
        params = request.values
        for key in params:
            if key == 'owner' or key == 'city':
                return jsonify(msg="You may not update the %s." % key), 409
            if key == 'updated_at' or key == 'created_at':
                continue
            else:
                setattr(place, key, params.get(key))
        place.save()
        return jsonify(msg="Place information updated successfully."), 200

    elif request.method == 'DELETE':
        try:
            get_place = Place.get(Place.id == id)
            get_place.delete_instance()
            return "Place with id = %d was deleted\n" % (int(id))
        except:
            return make_response(jsonify({'code': '10001', 'msg': 'no place found with that id'}), 404)


# def modify_place(place_id):
#     try:
#         id = place_id
#         if request.method == 'GET':
#             return jsonify(Place.get(Place.id == id).to_hash())
#     except:
#         return make_response(jsonify({'code': '10001',
#                                       'msg': 'no place found'}), 404)
#
#     if request.method == 'PUT':
#         id = place_id
#         try:
#             # uptading name
#             query = Place.update(name=request.form['name']).where(Place.id == id)
#             query.execute()
#         except:
#             pass
#         try:
#             # updating description
#             query = Place.update(description=request.form['description']).where(Place.id == id)
#             query.execute()
#         except:
#             pass
#
#         try:
#             # updating user last_name
#             query = Place.update(number_rooms=request.form['number_rooms']).where(Place.id == id)
#             query.execute()
#         except:
#             pass
#         try:
#             # updating and securing the password
#             query = Place.update(number_bathrooms=request.form['number_bathrooms']).where(Place.id == id)
#             query.execute()
#         except:
#             pass
#         try:
#             query = Place.update(max_guest=request.form['max_guest']).where(Place.id == id)
#             query.execute()
#         except:
#             pass
#         try:
#             query = Place.update(price_by_night=request.form['price_by_night']).where(Place.id == id)
#             query.execute()
#         except:
#             pass
#         try:
#
#             query = Place.update(latitude=request.form['latitude']).where(Place.id == id)
#             query.execute()
#         except:
#             pass
#         try:
#
#             query = Place.update(longitude=request.form['longitude']).where(Place.id == id)
#             query.execute()
#         except:
#             pass
#             # returning message when trying to update owner or city
#         if request.form['owner']:
#             return make_response(jsonify({'code': '10001',
#                                           'msg': 'owner can not be updated'}), 409)
#         elif request.form['city']:
#             return make_response(jsonify({'code': '10001',
#                                           'msg': 'city can not be updated'}), 409)
#         query.execute()
#         return "updated\n"
