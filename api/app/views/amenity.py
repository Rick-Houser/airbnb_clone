from app import app
from flask import Flask, jsonify, request
from datetime import datetime
from app.models.place import Place
from app.models.amenity import Amenity
from app.models.place_amenity import PlaceAmenities


# Get list of amenities
@app.route('/amenities', methods=['GET'])
def list_amenities():
    try:
        amenity_list = []
        for item in Amenity.select():
            amenity_list.append(item.to_dict())
            return jsonify(amenity_list)
    except:
        return jsonify({'code': 404, 'msg': 'not found'}), 404


# Create a new amenity from POST data parameters
@app.route('/amenities', methods=['POST'])
def create_amenity():
    # try:
    new_amenity = Amenity(name=request.form['name'])
    new_amenity.save()
    return jsonify(new_amenity.to_dict())
    # except:
    #     return jsonify({'code': 10003, 'msg': 'Name already exists'}), 409


# Get amenity by id
@app.route('/amenities/<amenity_id>', methods=['GET'])
def find_amenity(amenity_id):
    try:
        amenity = Amenity.get(Amenity.id == amenity_id)
        return jsonify(amenity.to_dict())
    except:
        return jsonify({'code': 404, 'msg': 'not found'}), 404


# Delete amenity
@app.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    try:
        amenity = Amenity.get(Amenity.id == amenity_id)
        amenity.delete_instance()
        return jsonify({'msg': 'Deleted amenity!'})
    except:
        return jsonify({'code': 404, 'msg': 'not found'}), 404


# Get list of amenities for selected place
@app.route('/places/<place_id>/amenities', methods=['GET'])
def list_select_amenities(place_id):
    try:
        Place.get(Place.id == place_id)
    except Place.DoesNotExist:
        return jsonify({'code': 404, 'msg': ' place not found'}), 404

    list = []
    get_amenity = (Amenity.select()
                   .join(PlaceAmenities)
                   .where(Amenity.id == PlaceAmenities.amenity)
                   .where(PlaceAmenities.place == place_id))
    for item in get_amenity:
        list.append(item.to_dict())
    return jsonify(list)


@app.route('/places/<place_id>/amenities/<amenity_id>',
           methods=['POST', 'DELETE'])
def update(place_id, amenity_id):
    # Checking if place exist
    try:
        Place.get(Place.id == place_id)
    except Place.DoesNotExist:
        return jsonify({'code': 404, 'msg': 'Place not found'}), 404

    # Checking is Amenity exist
    try:
        Amenity.get(Amenity.id == amenity_id)
    except Amenity.DoesNotExist:
        return jsonify({'code': 404, 'msg': 'Amenity not found'}), 404

    if request.method == "POST":
        new_place_amenity = PlaceAmenities(place=place_id, amenity=amenity_id)
        new_place_amenity.save()
        return jsonify(new_place_amenity.amenity.to_dict())

    elif request.method == "DELETE":
        get_place_a = PlaceAmenities.get(PlaceAmenities.place == place_id and
                                         PlaceAmenities.amenity == amenity_id)
        get_place_a.delete_instance
        return "amenity deleted"
