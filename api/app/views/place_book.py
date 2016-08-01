from app import app
from app.models.place_book import PlaceBook
from flask import Flask, jsonify, request
from datetime import datetime

# List all books for a selected place
@app.route('/places/<place_id>/books/', methods=["GET"])
def find_book(place_id):
	try:
		books = PlaceBook.select().where(PlaceBook.place == place_id)
		book_list = []
		for book in books:
			book_list.append(book.to_dict())
		return jsonify(book_list)
	except:
		return jsonify({'code': 404,'msg': 'not found'}), 404

# Create a new booking from POST data for a selected place
@app.route('/places/<place_id>/books/', methods=["POST"])
def create_book(place_id):
	try:
		data = request.values
		new_book = PlaceBook(
			place = place_id,
		 	user = data['user_id'],
		 	date_start = datetime.strptime(data['date_start'], "%Y/%m/%d %H:%M:%S"),
		 	number_nights = data['number_nights'],
		 	is_validated = data['is_validated'])
		new_book.save()
		return new_book.to_dict()
	except:
		return jsonify({'code': 404,'msg': 'not found'}), 404

# Find a booking
@app.route('/places/<int:place_id>/books/<book_id>', methods=['GET'])
def find_booking(place_id, book_id):
	try:
		booking = PlaceBook.get(PlaceBook.id == book_id)
		return booking.to_dict()
	except:
		return jsonify({'code': 404,'msg': 'not found'}), 404

# Modify a booking
@app.route('/places/<int:place_id>/books/<int:book_id>', methods=['PUT'])
def modify_booking(place_id, book_id):
	try:
		booking = PlaceBook.get(PlaceBook.id == book_id)
		data = request.values()
		for key in data:
			if key == 'user':
				return jsonify({'code': 405,'msg': 'Method not allowed'}), 405
			elif key == 'date_start':
				booking.date_start = datetime.strptime(data[key], "%Y/%m/%d %H:%M:%S")
			elif key == 'number_nights':
				booking.number_nights = data[key]
			elif key == 'is_validated':
				booking.is_validated = data[key]
		booking.save()
		return booking.to_dict()
	except:
		return jsonify({'code': 404,'msg': 'not found'}), 404

# Delete a booking
@app.route('/places/<int:place_id>/books/<int:book_id>', methods=['DELETE'])
def delete_booking(place_id, book_id):
	try:
		booking = PlaceBook.get(PlaceBook.id == book_id)
		booking.delete_instance()
		return jsonify({'msg': 'Deleted booking!'}), 200
	except:
		return jsonify({'code': 404,'msg': 'not found'}), 404
