from flask_flaat import UserMixin
from sqlalchemy import Column, Text
from . import database


class User(UserMixin, database.Model):
    sub = Column(Text, primary_key=True, nullable=False)
    iss = Column(Text, primary_key=True, nullable=False)
    email = Column(Text, unique=False, nullable=False)
    admin = Column(Text, unique=False, default=False)

    def get_id(self):
        """Overrides UserMixin to return token primary key. Value to store
        in cookie param '_user_id' when using flask_login.login_user 
        and to be collected later by login_manager.user_loader
        """
        return (self.token_sub, self.token_iss)


class Admin(User):
    def __init__(self, *args, admin=None, **kwargs):
        if admin:
            raise KeyError("Do not use admin in Admin")
        super().__init__(*args, admin=True, **kwargs)
