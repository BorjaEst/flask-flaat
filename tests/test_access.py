import pytest
from example import create_app


configs = [{
    'SECRET_KEY': 'not-so-secret-for-testing',
    'OIDC_CLIENT_ID': "test-oidc-client",
    'OIDC_CLIENT_SECRET': "not-so-secret-for-testing"
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


def test_public_access(client):
    response = client.get('/public')
    assert response.status_code == 204


def test_user_access(client):
    response = client.get('/users')
    assert response.status_code == 204


def test_admin_access(client):
    response = client.get('/admins')
    assert response.status_code == 204
