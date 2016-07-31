from app import app
from app.models.place_book import PlaceBook
from flask import Flask, jsonify, request
from datetime import datetime

# Get list of amenities
@app.route('/amenities', methods=['GET'])
def list_amenities():
	try:
		amenity_list = []
		for item in Amenity.select():
			amenity_list.append(item.to_hash())
		return jsonify(amenity_list)
	except:
		return jsonify({'code': 404,'msg': 'not found'}), 404

# Create a new amenity from POST data parameters
@app.route('/amenities', methods=['POST'])
def create_amenity():
	try:
		amenities = request.values()
		new_amenity = Amenity.create(name = amenities['name'])
		new_amenity.save()
		return jsonify(new_amenity.to_hash())
	except:
		return jsonify({'code': 10003,'msg': 'Name already exists'}), 409

# Get amenity by id
@app.route('/amenities/<amenity_id>', methods=['GET'])
	def find_amenity(amenity_id):
		try:
			amenity = Amenity.get(Amenity.id == amenity_id)
			return jsonify(amenity.to_hash())
		except:
			return jsonify({'code': 404,'msg': 'not found'}), 404

# Delete amenity
@app.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
	try:
		amenity = Amenity.get(Amenity.id == amenity_id)
		amenity.delete_instance()
		return jsonify({'msg': 'Deleted amenity!'})
	except:
		return jsonify({'code': 404,'msg': 'not found'}), 404

# Get list of amenities for selected place
@app.route('/places/<place_id>/amenities', methods=['GET'])
def list_select_amenities(place_id):
	try:
		select_amenity_list = []
		for item in PlaceAmenities.select().where(PlaceAmenities.place == place_id):
			select_amenity_list.append(item.to_hash())
		return jsonify(select_amenity_list)
	except:
		return jsonify({'code': 404,'msg': 'not found'}), 404
