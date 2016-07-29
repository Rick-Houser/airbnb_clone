from peewee import *
from user import User
from review_user import ReviewUser
from review_place import ReviewPlace


class Review(BaseModel):
    message = TextField(null=False)
    starts = IntegerField(default=0)
    user = ForeignKeyField(User, related_name="reviews", on_delete=cascade)

    def to_hash(self):
        return {'id': self.id,
                'created_at': self.created_at,
                'updated_at': self.updated_at,
                'message': self.message,
                'stars': self.starts,
                'from_user_id': self.user.id,
                'to_user_id': self.review_user.id,
                'to_place_id': self.review_place.id}
