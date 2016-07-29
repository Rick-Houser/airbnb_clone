from peewee import *
from user import User
from review_user import ReviewUser
from review_place import ReviewPlace


class Review(BaseModel):
    message = TextField(null=False)
    stars = IntegerField(default=0)
    user = ForeignKeyField(User, related_name="reviews", on_delete=cascade)

    def to_hash(self):
        data = {'id': self.id,
                'created_at': self.created_at,
                'updated_at': self.updated_at,
                'message': self.message,
                'stars': self.stars,
                'from_user_id': self.user,
                'to_user_id': self.id,
                'to_place_id': self.id}
        # try:
        #     query = (ReviewUser.select()
        #                        .join(Review)
        #                        .where(Review.id == review)
        #                        .get())
        #     data['from_user_id'] = query.user.id
        # except ReviewUser.DoesNotExist:
        #     data['from_user_id'] = None

        try:
            user_query = (ReviewUser.select()
                                    .join(User)
                                    .where(User.id == user)
                                    .get())
            data['to_user_id'] = user_query.user.id
        except ReviewUser.DoesNotExist:
            data['to_user_id'] = None

        try:
            place_query = (ReviewPlace.select()
                                      .join(Place)
                                      .where(Place.id == place)
                                      .get())
            data['to_place_id'] = place_query.place.id
        except ReviewPlace.DoesNotExist:
            data['to_place_id'] = None
        return data
