"""Module containing the different configurations"""


class Default(object):
    TESTING = True
    SECRET_KEY = "not-so-secret-for-testing"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    API_TITLE = 'Flask Flaat example'
    API_VERSION = 'v1'
    OPENAPI_VERSION = "3.0.2"
    OPENAPI_JSON_PATH = "api-spec.json"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    API_SPEC_OPTIONS = {}
    API_SPEC_OPTIONS['security'] = [{"bearerAuth": []}]
    API_SPEC_OPTIONS['components'] = {
        "securitySchemes": {
            "bearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT"
            }
        }
    }





class Configuration_1(Default):
    CLIENT_ID = "production-oidc-client"
    CLIENT_SECRET = "secret-example"
    ADMIN_ENTITLEMENTS = ["urn:admins"]
