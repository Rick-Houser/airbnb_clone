from app.models.review import Review
from app.models.review_place import ReviewPlace
from app.models.review_user import ReviewUser
from app.models.user import User
from app.models.place import Place
from app import app
from flask import jsonify, request
from flask import make_response
import json


@app.route('/users/<user_id>/reviews', methods=['GET', 'POST'])
def get_reviews_user(user_id):
    try:
        User.select().where(User.id == user_id).get()
    except User.DoesNotExist:
        return jsonify(msg="There is no user with this id."), 404
    # Getting all the review by user id
    if request.method == "GET":
        try:
            list = []
            # retriving the reviews an user received
            for review_user in ReviewUser.select().where(ReviewUser.user == user_id):
                list.append(review_user.review.to_hash())
            return jsonify(list)
        except:
                return make_response(jsonify({'code': 10000,
                                              'msg': 'Review not found'}), 404)

    elif request.method == "POST":
        user_message = request.form["message"]
        user_stars = request.form["stars"]

        try:
            new_review = Review(message=user_message,
                                stars=user_stars,
                                user=user_id)
            new_review.save()

            user_review = ReviewUser(user=user_id, review=new_review.id)
            user_review.save()

            return jsonify(new_review.to_hash())
        except:
            return make_response(jsonify({'code': 10000,
                                          'msg': 'Review not found'}), 404)


@app.route('/users/<user_id>/reviews/<review_id>', methods=['GET', 'DELETE'])
def delete_reviews_user(user_id, review_id):
    try:
        get_review = (ReviewUser.select()
                                .where((ReviewUser.review == review_id) &
                                       (ReviewUser.user == user_id)).get())

    except:
        return make_response(jsonify({'code': 10000,
                                      'msg': 'Review not found'}), 404)
    if request.method == 'GET':
        return jsonify(get_review.review.to_hash())

    elif request.method == 'DELETE':
        try:
            user_review = ReviewUser.get((ReviewUser.user == user_id) &
                                         (ReviewUser.review == review_id))
            user_review.delete_instance()

            get_review = Review.get(Review.id == review_id)
            get_review.delete_instance()
            return "Review was deleted"
        except:
            return make_response(jsonify({'code': 10000,
                                          'msg': 'Review not found'}), 404)


@app.route('/places/<place_id>/reviews', methods=['GET', 'POST'])
def get_review_place(place_id):
    try:
        # Checking if place exist
        Place.select().where(Place.id == place_id).get()
    except Place.DoesNotExist:
        return make_response(jsonify({'code': 10000,
                                      'msg': 'Place not found'}), 404)
    if request.method == 'GET':
        try:
            list = []
            for review_place in (ReviewPlace
                                 .select()
                                 .where(ReviewPlace.place == place_id)):
                list.append(review_place.review.to_hash())
            return jsonify(list)
        except:
            return make_response(jsonify({'code': 10000,
                                          'msg': 'Review not found'}), 404)
    elif request.method == 'POST':
        user_message = request.form["message"]
        user_stars = request.form["stars"]
        try:
            new_review = Review(message=user_message,
                                stars=user_stars,
                                user=place_id)  # using the place_id as user?
            new_review.save()

            review_place = ReviewPlace(review=new_review.id, place=place_id)
            review_place.save()
            return jsonify(new_review.to_hash())
        except:
            return make_response(jsonify({'code': 10000,
                                          'msg': 'Review not found'}), 404)


@app.route('/places/<place_id>/reviews/<review_id>', methods=['GET', 'DELETE'])
def delete_reviews_place(place_id, review_id):
    try:
        # Checking if place exist
        Place.select().where(Place.id == place_id).get()
    except Place.DoesNotExist:
        return make_response(jsonify({'code': 10000,
                                      'msg': 'Not found'}), 404)
    if request.method == 'GET':
        try:
            list = []
            for review_place in (ReviewPlace
                                 .select()
                                 .where(ReviewPlace.place == place_id,
                                        ReviewPlace.review == review_id)):
                list.append(review_place.review.to_hash())

            # Checking if the review is empty
            if len(list) == 0:
                return make_response(jsonify({'code': 10000,
                                              'msg': 'Review not found'}), 404)
            return jsonify(list)
        except:
            return make_response(jsonify({'code': 10000,
                                          'msg': 'Review not found'}), 404)
    elif request.method == 'DELETE':
        try:
            place_review = (ReviewPlace
                            .get(ReviewPlace.place == place_id &
                                 ReviewPlace.review == review_id))
            place_review.delete_instance()

            get_review = Review.get(Review.id == review_id)
            get_review.delete_instance()
            return "Review was deleted"
        except:
            return make_response(jsonify({'code': 10000,
                                          'msg': 'Review not found'}), 404)
