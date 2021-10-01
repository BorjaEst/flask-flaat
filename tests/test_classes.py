import pytest


class UsesLogin():
    @pytest.fixture(scope="class", autouse=True)
    def login(self, client):
        return client.get('/user/login')

    @pytest.fixture(scope="function")
    def logout(self, client, login):
        client.get('/user/logout')

    def test_correct_login(self, login):
        assert login.status_code == 204

    def test_correct_logout(self, logout):
        assert logout.status_code == 204
