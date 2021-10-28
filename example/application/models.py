from flask_flaat import UserMixin
from sqlalchemy import Column, Text
from . import database


class User(UserMixin, database.Model):
    sub = Column(Text, primary_key=True, nullable=False)
    iss = Column(Text, primary_key=True, nullable=False)
    email = Column(Text, unique=False, nullable=False)
