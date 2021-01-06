from ..modules.fma_contents import fma_contents

# Below schemas used for correctness nested parts. Error not used is normal.
# This error is kind of marshmallow feature error.
from application.schemas.locales_global import LocaleGlobalSchema  # noqa: 401
from .views import ViewsSchema  # noqa:401

from ..models.contents import ContentModel

class ContentSchema(fma_components.SQLAlchemyAutoSchema):  # noqa
    '''
    The schema used for reguliar component creation and for 'information' dump.
    '''
    locale = fma_contents.Nested('LocaleGlobalSchema', many=False)
    kind = fma_contents.Nested('ComponentKindSchema', many=False)

    class Meta:
        model = ContentModel
        # load_only = ('role_id', 'locale_id',)
        # exclude = ('password_hash',)
        # dump_only = ("id",)

        include_fk = True
        load_instance = True


component_schema = ContentSchema()


class ContentGetSchema(fma_components.SQLAlchemyAutoSchema):  # noqa
    '''
    The schema used for searching criterion on get method and other auxiliary purposes.
    No load instance and nested schemas.
    '''
    # locale = fma_components.Nested('LocaleGlobalSchema', many=False)

    class Meta:
        model = ContentModel
        # load_only = ('role_id', 'locale_id',)
        # exclude = ('title', 'content',)
        # load_only = ('locale_id',)
        # dump_only = ("id",)

        include_fk = True
        # load_instance = True


component_get_schema = ContentGetSchema()
