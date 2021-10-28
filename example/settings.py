"""Module containing the different configurations"""


class Default(object):
    TESTING = False
    SECRET_KEY = "not-so-secret-for-testing"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMINS_GROUP = "admins"
    ADMINS_CLAIM = "groups"


class Production(Default):
    CLIENT_ID = "production-oidc-client"
    CLIENT_SECRET = "secret-example"


class Development(Default):
    CLIENT_ID = "development-oidc-client"
    CLIENT_SECRET = "secret-example"


class Testing(Production):
    TESTING = True
