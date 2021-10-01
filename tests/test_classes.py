import pytest


class UsesLogin():
    @pytest.fixture(scope="class", autouse=True)
    def login(self, client):
        return client.get('/user/login')

    @pytest.fixture(scope="class")
    def logout(self, client, login):
        client.get('/user/logout')

    @pytest.mark.usefixtures('login')
    def test_correct_login(self, login):
        assert login.status_code == 204

    @pytest.mark.usefixtures('login')
    def test_correct_logout(self, logout):
        assert logout.status_code == 204
