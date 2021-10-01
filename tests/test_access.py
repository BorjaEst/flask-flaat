from .test_classes import UsesLogin


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
