from peewee import *
from user import User
from base import *
# from place import Place
# from review_user import ReviewUser
# from review_place import ReviewPlace

'''
 Review:
    - message: text field, cannot be blank
    - stars: int, set to 0 by default
    - user: foreign key to User
'''
class Review(BaseModel):
    message = TextField(null=False)
    stars = IntegerField(default=0)
    user = ForeignKeyField(User, related_name="reviews", on_delete='cascade')

    def to_dict(self):
        from review_user import ReviewUser
        from review_place import ReviewPlace

        data = {'id': self.id,
                'created_at': str(self.created_at.strftime('%d/%m/%Y %H:%M:%S')),
                'updated_at': str(self.updated_at.strftime('%d/%m/%Y %H:%M:%S')),
                'message': self.message,
                'stars': self.stars,
                'from_user_id': self.user.id,
                'to_user_id': self.id,
                'to_place_id': self.id
                }

        try:
            user_query = (ReviewUser.select()
                                    .where(ReviewUser.review == self.id)
                                    .get())  # .join(User)
            data['to_user_id'] = user_query.user.id
        except ReviewUser.DoesNotExist:
            data['to_user_id'] = None

        try:
            place_query = (ReviewPlace.select()
                                      .where(ReviewPlace.review == self.id)
                                      .get())  # .join(Place)
            data['to_place_id'] = place_query.place.id
        except ReviewPlace.DoesNotExist:
            data['to_place_id'] = None
        return data
