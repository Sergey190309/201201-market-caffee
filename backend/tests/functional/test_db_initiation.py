import pytest

from sqlalchemy import create_engine, MetaData, Table, select
from application.testing_config import SQLALCHEMY_DATABASE_URI


@pytest.fixture
def url_users(root_url):
    '''
    Generate url for this file tests.
    '''
    return root_url + '/home/index'


@pytest.fixture
def post_json():
    '''
    Generate json for file tests.
    '''

    return {
        "email": "s@gmail.com",
        "password": "qwer"
    }


@pytest.fixture
def _app_folder():
    '''
    Used as an addendum to generate SQLite file path.
    '''
    return 'application/'


@pytest.fixture
def _engine(_app_folder):
    '''
    Generation of SQLite file path.
    '''
    URI_cuts = SQLALCHEMY_DATABASE_URI.split('///')
    URI = URI_cuts[0] + '///' + _app_folder + URI_cuts[1]
    return create_engine(URI)
    # return create_engine(URI, echo=True)


# @pytest.mark.active
@pytest.mark.init_db
def test_client(
    test_client, url_users,
    post_json
):
    resp = test_client.get(url_users)
    # resp = test_client.get(url_users, json=post_json)
    assert resp.status_code == 200


@pytest.mark.init_db
def test_db_creation(
    _engine
):
    '''
    Test checks all tables availability
    '''
    tables = _engine.table_names()

    table_names = [
        'locales',
        'confirmations',
        'roles',
        'users'
    ]
    assert tables.sort() == table_names.sort()


@pytest.mark.active
@pytest.mark.init_db
@pytest.mark.parametrize(
    'id, remark',
    [
        ('user', 'Registered user after confirmation.'),
        ('power_user', 'By admin decision.'),
        ('admin', 'By owners decision.')
    ]
)
def test_roles(
    id, remark,
    _engine, table_name='roles'
):
    '''
    Test checks role table contents.
    '''
    meta = MetaData()
    table = Table(table_name, meta, autoload=True, autoload_with=_engine)

    stmt = select([table]).where(table.columns.id == id)

    with _engine.connect() as conn:
        result = conn.execute(stmt).fetchone()

    assert result[1] == remark


@pytest.mark.active
@pytest.mark.init_db
@pytest.mark.parametrize(
    'id, remark',
    [
        ('ru', 'Общий русский.'),
        ('en', 'General english.')
    ]
)
def test_locales(
    id, remark,
    _engine, table_name='locales'
):
    '''
    Test checks role table contents.
    '''
    meta = MetaData()
    table = Table(table_name, meta, autoload=True, autoload_with=_engine)

    stmt = select([table]).where(table.columns.id == id)

    with _engine.connect() as conn:
        result = conn.execute(stmt).fetchone()

    assert result[1] == remark
