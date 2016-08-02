from app import app
from app.models.place_book import PlaceBook
from flask import Flask, jsonify, request
from datetime import datetime
from app.models.place import Place


@app.route('/places/<place_id>/books', methods=["GET", "POST"])
# List all books for a selected place
def find_book(place_id):
    # Checking if the place exist
    try:
        Place.get(Place.id == place_id)
    except Place.DoesNotExist:
        return jsonify({'code': 404, 'msg': 'Place not found'}), 404

    if request.method == "GET":
        try:
            # Selecting the place booked
            books = PlaceBook.select().where(PlaceBook.place == place_id)
            book_list = []
            for book in books:
                book_list.append(book.to_dict())
                return jsonify(book_list)
        except:
            return jsonify({'code': 404, 'msg': 'Book not found'}), 404
    if request.method == "POST":
        try:
            # Create a new booking from POST data for a selected place
            get_user = request.form['user_id']
            get_date = request.form['date_start']
            get_nights = request.form['number_nights']
            new_book = PlaceBook(place=place_id,
                                 user=get_user,
                                 date_start=get_date,
                                 number_nights=get_nights)
            new_book.save()
            return jsonify(new_book.to_dict())

        except:
            return jsonify({'code': 404, 'msg': 'not found'}), 404


@app.route('/places/<int:place_id>/books/<book_id>', methods=['GET'])
def find_booking(place_id, book_id):
    # Checking if the place exist
    try:
        Place.get(Place.id == place_id)
    except Place.DoesNotExist:
        return jsonify({'code': 404, 'msg': 'Place not found'}), 404

    # Checking if the booking exist
    try:
        PlaceBook.get(PlaceBook.id == book_id)
    except PlaceBook.DoesNotExist:
        return jsonify({'code': 404, 'msg': 'Booking not found'}), 404
    # Find a booking
    try:
        booking = PlaceBook.get(PlaceBook.id == book_id and
                                PlaceBook.place == place_id)
        return jsonify(booking.to_dict())
    except:
        return jsonify({'code': 404, 'msg': 'not found'}), 404


@app.route('/places/<int:place_id>/books/<int:book_id>', methods=['PUT'])
def modify_booking(place_id, book_id):
    # Modify a booking
    try:
        booking = PlaceBook.get(PlaceBook.id == book_id)
        data = request.form
        for key in data:
            if key == 'user_id':
                return jsonify({'code': 405, 'msg': 'Method not allowed'}), 405
            elif key == 'date_start':
                booking.date_start = data[key]
            elif key == '`number_nights`':
                booking.number_nights = data[key]
            elif key == 'is_validated':
                booking.is_validated = data[key]
            booking.save()
        return jsonify(booking.to_dict())
    except:
        return jsonify({'code': 404, 'msg': 'not found'}), 404


@app.route('/places/<int:place_id>/books/<int:book_id>', methods=['DELETE'])
def delete_booking(place_id, book_id):
    # Checking if the place exist
    try:
        Place.get(Place.id == place_id)
    except Place.DoesNotExist:
        return jsonify({'code': 404, 'msg': 'Place not found'}), 404

    # Checking if the booking exist
    try:
        PlaceBook.get(PlaceBook.id == book_id)
    except PlaceBook.DoesNotExist:
        return jsonify({'code': 404, 'msg': 'Booking not found'}), 404
    # Delete a booking
    try:
        booking = PlaceBook.get(PlaceBook.id == book_id and
                                PlaceBook.place == place_id)
        booking.delete_instance()
        return jsonify({'msg': 'Booked place was deleted'}), 200
    except:
        return jsonify({'code': 404, 'msg': 'not found'}), 404


@app.route('/places/<place_id>/book', methods=['POST'])
def booked(place_id):
    if request.method == 'POST':
        PlaceBook.get(PlaceBook.place == place_id)
