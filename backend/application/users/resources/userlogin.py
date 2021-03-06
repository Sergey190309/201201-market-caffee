from typing import Dict

from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
    get_raw_jwt,
    get_jwt_identity,
    jwt_required,
    jwt_refresh_token_required
)
from flask_babelplus import lazy_gettext as _
# from ..modules.fbc import fbc

from ..models.users import UserModel
from ..modules.blacklist import BLACKLIST


class UserLogin(Resource):
    @classmethod
    def post(cls) -> Dict:
        '''
        LogIn
        '''
        _json = request.get_json()
        _user = UserModel.find_by_email(_json['email'])
        # print('UserLogin.post')
        if _user is None:
            return {
                'message': str(_(
                    "User with email '%(email)s' has not been found.",
                    email=_json['email'])),
            }, 404
        else:
            if not _user.check_password(_json['password']):
                return {
                    'message': str(_(
                        "Wrong password for user with email '%(email)s'.",
                        email=_json['email'])),
                }, 400
                print('UserLogin.post user.role_id -', _user.role_id)
            else:
                if not _user.is_valid:
                    return {
                        'message': str(_(
                            "It seems you have not confirm your account. "
                            "Check email stated - '%(email)s'.",
                            email=_json['email'])),
                    }, 400
        _user.set_accessed()
        return {
            'message': str(_(
                "You are welcome, tokens are in payload.")),
            'payload': _user.get_tokens()
        }, 200

    @classmethod
    @jwt_required
    def put(cls) -> Dict:
        '''
        LogOut
        '''
        jti = get_raw_jwt()['jti']  # jti is "JWT ID", a unique
        # identifier for a JWT.
        BLACKLIST.add(jti)
        return {"message": str(_("Successfully logged out."))}, 200

    @classmethod
    @jwt_refresh_token_required
    def patch(cls):
        '''
        Token refresh
        '''
        _user = UserModel.find_by_id(get_jwt_identity())
        if not _user:
            return {
                'message': str(_(
                    'Something wrong with token refreshing. Try to log in again.')),
            }, 500
        return {
            'message': str(_('Token successfully refreshed.')),
            'payload': {
                'access_token': _user.get_fresh_token()
            }
        }, 200
