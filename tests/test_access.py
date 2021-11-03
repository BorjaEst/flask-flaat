import pytest
from example.application import models

from .test_classes import UsesLogin, NeedsAdmin

user = dict(sub='user', iss='iss', email="user@iss.com")


@pytest.fixture(scope="module", autouse=True, params=[user])
def create_user(request, db):
    user = models.User(**request.param)
    db.session.add(user)
    db.session.commit()
    return user


class TestAsPublic():

    def test_public_resource(self, client):
        response = client.get('/resource/public')
        assert response.status_code == 204

    def test_user_resource(self, client):
        response = client.get('/resource/users')
        assert response.status_code == 401

    def test_admin_resource(self, client):
        response = client.get('/resource/admins')
        assert response.status_code == 401

    def test_user_login(self, client):
        response = client.get('/user/login')
        assert response.status_code == 401

    def test_user_logout(self, client):
        response = client.get('/user/logout')
        assert response.status_code == 401


@pytest.mark.parametrize('token_sub', ['unknown'], indirect=True)
@pytest.mark.parametrize('token_iss', ['unknown'], indirect=True)
class TestUnknownUser():
    @pytest.fixture(scope="class")
    def headers(self, access_token):
        return {'Authorization': 'Bearer {}'.format(access_token)}

    def test_public_resource(self, client, headers):
        response = client.get('/resource/public', headers=headers)
        assert response.status_code == 204

    def test_user_resource(self, client, headers):
        response = client.get('/resource/users', headers=headers)
        assert response.status_code == 401

    def test_admin_resource(self, client, headers):
        response = client.get('/resource/admins', headers=headers)
        assert response.status_code == 401


@pytest.mark.parametrize('token_sub', [user['sub']], indirect=True)
@pytest.mark.parametrize('token_iss', [user['iss']], indirect=True)
class TestUsingUserToken():
    @pytest.fixture(scope="class")
    def headers(self, access_token):
        return {'Authorization': 'Bearer {}'.format(access_token)}

    def test_public_resource(self, client, headers):
        response = client.get('/resource/public', headers=headers)
        assert response.status_code == 204

    def test_user_resource(self, client, headers):
        response = client.get('/resource/users', headers=headers)
        assert response.status_code == 204

    def test_admin_resource(self, client, headers):
        response = client.get('/resource/admins', headers=headers)
        assert response.status_code == 403


@pytest.mark.parametrize('token_sub', [user['sub']], indirect=True)
@pytest.mark.parametrize('token_iss', [user['iss']], indirect=True)
class TestLoggedAsUser(UsesLogin):

    def test_public_resource(self, client):
        response = client.get('/resource/public')
        assert response.status_code == 204

    def test_user_resource(self, client):
        response = client.get('/resource/users')
        assert response.status_code == 204

    def test_admin_resource(self, client):
        response = client.get('/resource/admins')
        assert response.status_code == 403


@pytest.mark.parametrize('token_sub', [user['sub']], indirect=True)
@pytest.mark.parametrize('token_iss', [user['iss']], indirect=True)
class TestUsingAdminToken(NeedsAdmin):
    @pytest.fixture(scope="class")
    def headers(self, access_token):
        return {'Authorization': 'Bearer {}'.format(access_token)}

    def test_public_resource(self, client, headers):
        response = client.get('/resource/public', headers=headers)
        assert response.status_code == 204

    def test_user_resource(self, client, headers):
        response = client.get('/resource/users', headers=headers)
        assert response.status_code == 204

    def test_admin_resource(self, client, headers):
        response = client.get('/resource/admins', headers=headers)
        assert response.status_code == 204


@pytest.mark.parametrize('token_sub', [user['sub']], indirect=True)
@pytest.mark.parametrize('token_iss', [user['iss']], indirect=True)
class TestLoggedAsAdmin(UsesLogin, NeedsAdmin):

    def test_public_resource(self, client):
        response = client.get('/resource/public')
        assert response.status_code == 204

    def test_user_resource(self, client):
        response = client.get('/resource/users')
        assert response.status_code == 204

    def test_admin_resource(self, client):
        response = client.get('/resource/admins')
        assert response.status_code == 204
