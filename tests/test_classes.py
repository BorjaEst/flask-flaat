import pytest


class UsesLogin():
    @pytest.fixture(scope="class", autouse=True)
    def login(self, client, access_token):
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        return client.get('/user/login', headers=headers)

    @pytest.fixture(scope="function")
    def logout(self, client, login):
        return client.get('/user/logout')

    def test_correct_login(self, login):
        assert login.status_code == 204

    def test_correct_logout(self, logout):
        assert logout.status_code == 204
