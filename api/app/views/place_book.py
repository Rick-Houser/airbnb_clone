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
    # Find a booking
    try:
        booking = PlaceBook.get(PlaceBook.id == book_id and
                                PlaceBook.place == place_id)
        return jsonify(booking.to_dict())
    except:
        return jsonify({'code': 404, 'msg': 'not found'}), 404


# @app.route('/places/<int:place_id>/books/<int:book_id>', methods=['PUT'])
# # Modify a booking
# def modify_booking(place_id, book_id):
# try:
# booking = PlaceBook.get(PlaceBook.id == book_id)
# data = request.values()
# for key in data:
# if key == 'user':
# return jsonify({'code': 405, 'msg': 'Method not allowed'}), 405
# elif key == 'date_start':
# booking.date_start = datetime.strptime(data[key], "%Y/%m/%d %H:%M:%S")
# elif key == 'number_nights':
# booking.number_nights = data[key]
# elif key == 'is_validated':
# booking.is_validated = data[key]
# booking.save()
# return booking.to_dict()
# except:
# return jsonify({'code': 404, 'msg': 'not found'}), 404
#
#
# @app.route('/places/<int:place_id>/books/<int:book_id>', methods=['DELETE'])
# # Delete a booking
# def delete_booking(place_id, book_id):
# try:
# booking = PlaceBook.get(PlaceBook.id == book_id)
# booking.delete_instance()
# return jsonify({'msg': 'Deleted booking!'}), 200
# except:
# return jsonify({'code': 404, 'msg': 'not found'}), 404
