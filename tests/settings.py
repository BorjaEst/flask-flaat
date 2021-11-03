"""Module containing the different configurations"""


class Default(object):
    TESTING = True
    SECRET_KEY = "not-so-secret-for-testing"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Configuration_1(Default):
    CLIENT_ID = "production-oidc-client"
    CLIENT_SECRET = "secret-example"
    ADMINS_GROUP = "admins"
    ADMINS_CLAIM = "groups"
