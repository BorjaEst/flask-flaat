import pytest
from example import models

from .test_classes import UsesLogin

user1 = dict(sub='u1', iss='iss', email="u1@iss.com")
admin = dict(sub='a1', iss='iss', email="a1@iss.com")


@pytest.fixture(scope="module", autouse=True, params=[user1])
def create_user(request, db):
    user = models.User(**request.param)
    db.session.add(user)
    db.session.commit()
    return user


@pytest.fixture(scope="module", autouse=True, params=[admin])
def create_admin(request, db):
    user = models.Admin(**request.param)
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


@pytest.mark.parametrize('token_sub', [user1['sub']], indirect=True)
@pytest.mark.parametrize('token_iss', [user1['iss']], indirect=True)
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


@pytest.mark.parametrize('token_sub', [user1['sub']], indirect=True)
@pytest.mark.parametrize('token_iss', [user1['iss']], indirect=True)
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


@pytest.mark.parametrize('token_sub', [admin['sub']], indirect=True)
@pytest.mark.parametrize('token_iss', [admin['iss']], indirect=True)
class TestUsingAdminToken():
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


@pytest.mark.parametrize('token_sub', [admin['sub']], indirect=True)
@pytest.mark.parametrize('token_iss', [admin['iss']], indirect=True)
class TestLoggedAsAdmin(UsesLogin):

    def test_public_resource(self, client):
        response = client.get('/resource/public')
        assert response.status_code == 204

    def test_user_resource(self, client):
        response = client.get('/resource/users')
        assert response.status_code == 204

    def test_admin_resource(self, client):
        response = client.get('/resource/admins')
        assert response.status_code == 204
