from typing import Dict, Union
# Global variables here:


class DefaultAdmin():
    '''
    Those credentials would be loaded with id = 1 and role = admin
    '''
    def __init__(self):
        self._admin = {
            'id': 1,
            'user_name': 'admin',
            'email': 'a@agatha-ng.com',
            'password': 'qwer',
            'role_id': 'admin',
            'locale_id': 'en',
            'time_zone': 3,
            'remarks': (
                "It's dummy admin to handle database. "
                "It's better, at least, to change email for "
                "real one and password for strong one."
            )
        }

    @property
    def get_default_admin(self):
        return self._admin


class GlobalConstants():
    '''
    The class contains constants that are accessible from all application.
    Currently those are:
    '''
    def __init__(self):
        self._ROLES = [
            {'id': 'user', 'remarks': 'Registered user after confirmation.'},
            {'id': 'power_user', 'remarks': 'By admin decision.'},
            {'id': 'admin', 'remarks': 'By owners decision.'}
        ]
        self._LOCALES = [
            {'id': 'ru', 'remarks': 'Общий русский.'},
            {'id': 'en', 'remarks': 'General english.'},

        ]

    @property
    def get_ROLES(self):
        return self._ROLES

    @property
    def get_LOCALES(self):
        return self._LOCALES


class GlobalVariables():
    '''
    The class contains variables that are accessible from all application.
    Currently those with default values are:
    'locale': 'en',
    'time_zone': 'ETC/GMT-3'

    '''
    def __init__(self, values: Dict = {
        # 'locale': 'ru',
        'locale': 'en',
        'time_zone': 'ETC/GMT-3'
    }):

        self.app_globals = values

    def set_globals(self, set_values: Dict):
        for item in set_values:
            # print(item)
            self.app_globals[item] = set_values[item]

    def get_global_by_name(self, get_what: str) -> Union[str, None]:
        # print('get_globals self.app_globals -', self.app_globals)
        if get_what in self.app_globals.keys():
            return self.app_globals[get_what]
        return None

    def get_globals(self) -> Dict:
        return self.app_globals