import pytest
from example import create_app

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
    app = create_app(application_configuration)
    with app.test_request_context():
        yield app


@pytest.fixture(scope="function")
def client(app):
    with app.test_client() as client:
        yield client
