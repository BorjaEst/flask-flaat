import pytest
import flaat


@pytest.fixture(scope="module", autouse=True)
def start_database(db):
    return


@pytest.mark.parametrize('token_sub', ['unknown'], indirect=True)
@pytest.mark.parametrize('token_iss', ['unknown'], indirect=True)
def test_incorrect_login(client, access_token):
    headers = {'Authorization': 'Bearer {}'.format(access_token)}
    response = client.get('/user/login', headers=headers)
    assert response.status_code == 401


@pytest.mark.parametrize('token_sub', ['unknown'], indirect=True)
@pytest.mark.parametrize('token_iss', ['unknown'], indirect=True)
def test_incorrect_logout(client, access_token):
    headers = {'Authorization': 'Bearer {}'.format(access_token)}
    response = client.get('/user/logout', headers=headers)
    assert response.status_code == 401


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
            lambda *args, **kwargs: {'eduperson_entitlement': ["urn:admins"]},
        )
