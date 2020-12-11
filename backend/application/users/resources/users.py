from typing import Dict

from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_babelplus import lazy_gettext as _

from ..schemas.users import UserSchema, UserUpdateSchema
from ..models.users import UserModel

user_schema = UserSchema()
user_update_schema = UserUpdateSchema()


class User(Resource):
    @classmethod
    def post(cls) -> Dict:
        '''
        Creates user based on json.
        '''
        # _json = request.get_json()
        # print('users.resources.users.User.post _json -', _json)
        _user = user_schema.load(request.get_json())
        if UserModel.find_by_email(_user.email):
            return {
                'message': str(_(
                    "User with email '%(email)s' already exists.",
                    email=_user.email)),
            }, 400
        else:
            _user.save_to_db()
            try:
                _created_user = UserModel.find_by_email(_user.email)
            except Exception as err:
                print('users.resources.User.post error\n', err)
            return {
                'message': str(_(
                    "User with email '%(email)s' created, details are in payload.",
                    email=_user.email)),
                'payload': user_schema.dump(_created_user)
            }, 201

    @classmethod
    @jwt_required
    def get(cls) -> Dict:
        '''
        Get all user details by email in json.
        Allowd for owner or admin.
        '''
        _json = request.get_json()
        # Below is for validation only.
        user_update_schema.load(_json)

        _email = _json['email']
        _user_logged = UserModel.find_by_id(get_jwt_identity())
        if not (_user_logged.is_admin or _user_logged.is_own_email(_email)):
            return {
                'message': str(_(
                    "Admins or account owner are allowed to see details "
                    "by email. You are neither admin not own this account."))
            }, 401

        _user = UserModel.find_by_email(_email)
        if _user:
            # print('users.resources.users.User.get _user -', user_schema.dump(_user))
            return {
                'message': str(_(
                    "User with email '%(email)s' found, details are "
                    "in payload.", email=_email)),
                'payload': user_schema.dump(_user)
            }, 200
        else:
            return {
                'message': str(_(
                    "User with email '%(email)s' has not been found.",
                    email=_email)),
            }, 404
