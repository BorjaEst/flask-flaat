import pytest
from example import create_app
from example import database

configs = [{
    'SECRET_KEY': 'not-so-secret-for-testing',
    'CLIENT_ID': "test-oidc-client",
    'CLIENT_SECRET': "not-so-secret-for-testing"
}]


@pytest.fixture(scope='session', params=configs)
def application_configuration(request):
    """Patch fixture to set test configuration variables."""
    return request.param


@pytest.fixture(scope="session")
def app(application_configuration):
    """Create application_configuration for the tests."""
    return create_app(application_configuration)


@pytest.fixture(scope="session")
def db(app):
    """Returns session-wide initialized database."""
    with app.app_context():
        database.create_all()
        yield database
        database.drop_all()


@pytest.fixture(scope="class")
def client(app):
    """Provides a http client for flask"""
    return app.test_client()


@pytest.fixture(scope="function")
def session(app, db):
    """Keeps test request open to rollback db changes"""
    with app.test_request_context():
        db.session.begin_nested()
        yield
        db.session.rollback()
