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


class TestPublicAccess():

    def test_public_access(self, client):
        response = client.get('/resource/public')
        assert response.status_code == 204


class TestUserAccess():
    @pytest.fixture(autouse=True)
    def login(self, client):
        return client.get('/user/login')

    @pytest.fixture()
    def logout(self, login):
        client.get('/user/logout')

    @pytest.mark.usefixtures('login')
    def test_correct_login(self, login):
        assert login.status_code == 204

    @pytest.mark.usefixtures('login')
    def test_correct_logout(self, logout):
        assert logout.status_code == 204

    def test_user_access(self, client):
        response = client.get('/resource/users')
        assert response.status_code == 204


class TestAdminAccess():
    def login(self, client):
        return client.get('/user/login')

    @pytest.fixture()
    def logout(self, login):
        client.get('/user/logout')

    @pytest.mark.usefixtures('login')
    def test_correct_login(self, login):
        assert login.status_code == 204

    @pytest.mark.usefixtures('login')
    def test_correct_logout(self, logout):
        assert logout.status_code == 204

    @pytest.mark.usefixtures('login')
    def test_admin_access(self, client):
        response = client.get('/resource/admins')
        assert response.status_code == 204
