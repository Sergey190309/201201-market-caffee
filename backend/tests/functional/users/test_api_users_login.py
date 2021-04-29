import pytest
from flask import url_for
# from application.users.models.users import UserModel


@pytest.fixture
def login_json(user_create_json):
    _user_create_json = user_create_json()
    return {
        "email": _user_create_json['email'],
        "password": _user_create_json['password']
    }


# @pytest.fixture
# def access_token():
#     def _method(user):
#         return user.get_tokens()['access_token']
#     return _method


@pytest.fixture
def refresh_token():
    def _method(user):
        return user.get_tokens()['refresh_token']
    return _method


# @pytest.mark.active
def test_user_login_post(
        client,
        created_user,
        login_json):

    # Create new user:
    _user = created_user(email=login_json['email'])
    assert _user is not None

    # login user is not valid
    resp = client.post(url_for('users_bp.userlogin'), json=login_json)
    assert resp.status_code == 400
    assert isinstance(resp.json['message'], str)
    assert 'message' in resp.json.keys()  # There is message in responce.
    assert not('payload' in resp.json.keys())  # No payload in the responce.

    # login user is valid
    _user.update({'role_id': 'user'})
    resp = client.post(url_for('users_bp.userlogin'), json=login_json)
    assert resp.status_code == 200
    assert 'message' in resp.json.keys()
    assert 'payload' in resp.json.keys()

    # login user does not exists
    login_json_wrong_email = login_json.copy()
    login_json_wrong_email['email'] = 'wrong@email.com'
    resp = client.post(url_for('users_bp.userlogin'), json=login_json_wrong_email)
    assert resp.status_code == 404
    assert 'message' in resp.json.keys()
    assert not('payload' in resp.json.keys())

    # login wrong password
    login_json_wrong_password = login_json.copy()
    login_json_wrong_password['password'] = 'wrong password'
    resp = client.post(url_for('users_bp.userlogin'), json=login_json_wrong_password)
    assert resp.status_code == 400
    assert 'message' in resp.json.keys()
    assert not('payload' in resp.json.keys())


# @pytest.mark.active
def test_user_login_delete(
        client,
        created_user,
        access_token):
    _user = created_user()
    headers = {'Authorization': f'Bearer {access_token(_user)}'}
    resp = client.delete(url_for('users_bp.userlogin'), headers=headers)
    # print(resp.json)
    assert resp.status_code == 200
    assert 'message' in resp.json.keys()


# @pytest.mark.active
def test_user_login_put(
        client,
        created_user,
        refresh_token):
    _user = created_user()
    headers = {'Authorization': f'Bearer {refresh_token(_user)}'}
    resp = client.put(url_for('users_bp.userlogin'), headers=headers)
    assert resp.status_code == 200
    assert 'message' in resp.json.keys()
    assert 'payload' in resp.json.keys()
    assert isinstance(resp.json['payload']['access_token'], str)
