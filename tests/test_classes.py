import pytest
import flaat


class UsesLogin():
    @pytest.fixture(scope="function", autouse=True)
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


class NeedsAdmin():
    @pytest.fixture(scope="class", autouse=True)
    def introspection_info(request, class_mocker):
        class_mocker.patch.object(
            flaat.Flaat, 'get_info_from_introspection_endpoints',
            lambda *args, **kwargs: {'groups': ['admins']},
        )
