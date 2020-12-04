from typing import Dict, Union
# Global variables here:

# app_locale = 'ru'


class GlobalVariables():

    def __init__(self, values: Dict = {
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
