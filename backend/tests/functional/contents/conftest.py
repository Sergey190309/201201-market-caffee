import pytest

from typing import Dict
from random import randint
# from random import choice, randint

from application.modules.dbs_global import dbs_global
from application.contents.models.contents import ContentModel
from application.contents.models.views import ViewModel
from application.contents.schemas.contents import ContentGetSchema, ContentSchema
from application.contents.schemas.views import ViewGetSchema, ViewSchema

from application.global_init_data import global_constants
from application.contents.local_init_data_contents import contents_constants
# from application.components.local_init_data_components import components_constants
# from application.users.local_init_data_users import users_constants


@pytest.fixture(scope='session')
def view_get_schema():
    return ViewGetSchema()


@pytest.fixture(scope='session')
def view_schema():
    return ViewSchema()


@pytest.fixture(scope='session')
def content_get_schema():
    return ContentGetSchema()


@pytest.fixture(scope='session')
def content_schema():
    return ContentSchema()


# @pytest.fixture(params=['main'])
@pytest.fixture(params=[item['id_view'] for item in contents_constants.get_VIEWS])
def allowed_view(request):
    return request.param


@pytest.fixture(scope='module')
def content_instance(random_text, random_text_underscore):
    '''
    Content model instance without saving.
    identity, view_id, locale_id - arguments, title - random set of 3 words.
    content - random set of 5 words
    '''
    def _method(content_ids: Dict = {}):
        # print(content_ids)
        keys = content_ids.keys()
        if 'identity' in keys:
            _identity = content_ids['identity']
        else:
            _identity = random_text_underscore(qnt=2)[0: -1]

        if 'view_id' in keys:
            _view_id = content_ids['view_id']
        else:
            _view_id = contents_constants.get_VIEWS[0]['id_view']

        if 'locale_id' in keys:
            _locale_id = content_ids['locale_id']
        else:
            _locale_id = global_constants.get_LOCALES[0]['id']

        if 'user_id' in keys:
            _user_id = content_ids['user_id']
        else:
            _user_id = randint(1, 128)

        if 'title' in keys:
            _title = content_ids['title']
        else:
            _title = random_text(_locale_id, 3)

        if 'content' in keys:
            _content = content_ids['content']
        else:
            _content = random_text(_locale_id, 5)

        return ContentModel(
            identity=_identity,
            view_id=_view_id,
            locale_id=_locale_id,
            user_id=_user_id,
            title=_title,
            content=_content)
    return _method


@pytest.fixture(scope='module')
def view_instance(random_text_underscore, random_text, view_schema):
    '''
    View model instance without saving.
    id_kind - argument or random text of 3 word to avoid repeating keys,
    description - argument or random set of 12 words.
    '''
    def _method(values: Dict = {}) -> 'ViewModel':
        if values is None or not isinstance(values, Dict):
            return 'Provide values in dictinary type'
        _json = {}
        keys = values.keys()
        if 'id_view' in keys:
            _json['id_view'] = values['id_view']
        else:
            _json['id_view'] = random_text_underscore(qnt=3)
        if 'description' in keys:
            _json['description'] = values['description']
        else:
            _json['description'] = random_text(qnt=12)
        return view_schema.load(_json, session=dbs_global.session)
    return _method
