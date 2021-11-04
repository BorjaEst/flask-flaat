import pytest
import flaat
from flask_flaat import current_userinfo


@pytest.fixture(scope="module", autouse=True)
def userendpoints_info(session_mocker):
    session_mocker.patch.object(
        flaat.Flaat, 'get_info_from_userinfo_endpoints',
        lambda *args, **kwargs: {'key1': 'value1'},
    )


@pytest.fixture(scope="module", autouse=True)
def introspection_info(session_mocker):
    session_mocker.patch.object(
        flaat.Flaat, 'get_info_from_introspection_endpoints',
        lambda *args, **kwargs: {'key2': 'value2'},
    )


@pytest.mark.parametrize('token_sub', ['user_sub'], indirect=True)
@pytest.mark.parametrize('token_iss', ['user_iss'], indirect=True)
def test_current_userinfo(app, access_token):
    headers = {'Authorization': 'Bearer {}'.format(access_token)}
    with app.test_request_context(headers=headers):
        assert current_userinfo['body']['sub'] == 'user_sub'
        assert current_userinfo['body']['iss'] == 'user_iss'
        assert current_userinfo['key1'] == 'value1'
        assert current_userinfo['key2'] == 'value2'
