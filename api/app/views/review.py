from app.models.review import Review
from app import app
from flask import jsonify, request
from flask import make_response


@app.route('/users/<user_id>/reviews', methods=['GET', 'POST'])
def get_reviews(user_id):
    id == user_id
    # Getting all the review by user id
    if request.method == "GET":
        try:
            list = []
            for review in Review.select().where(Review.user == id):
                list.append(review.to_hash)
            return jsonify(list)
        except:
                return make_response(jsonify({'code': 10000,
                                              'msg': 'Review not found'}), 404)

    elif request.method == "POST":
        user_message = request.form["message"]
        user_stars = request.form["stars"]
        user_id = id  # Not sure about this one

        try:
            new_review = Review(message=user_message,
                                stars=user_stars,
                                user=user_id)
        except:
            return make_response(jsonify({'code': 10000,
                                          'msg': 'Review not found'}), 404)
