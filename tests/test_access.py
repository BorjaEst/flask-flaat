import pytest
from example import models

from .test_classes import UsesLogin


@pytest.fixture(scope="module", autouse=True)
def user(db):
    user = models.User(sub='u1', iss='iss', email="u1@iss.com")
    db.session.add(user)
    db.session.commit()
    return user


@pytest.fixture(scope="module", autouse=True)
def admin(db):
    user = models.Admin(sub='a1', iss='iss', email="a1@iss.com")
    db.session.add(user)
    db.session.commit()
    return user


class TestPublicAccess():
    def test_public_access(self, client):
        response = client.get('/resource/public')
        assert response.status_code == 204


class TestUserAccess(UsesLogin):
    def test_user_access(self, client):
        response = client.get('/resource/users')
        assert response.status_code == 204


class TestAdminAccess(UsesLogin):
    def test_admin_access(self, client):
        response = client.get('/resource/admins')
        assert response.status_code == 204
