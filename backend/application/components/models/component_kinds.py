from typing import Dict
from application.modules.dbs_global import dbs_global


class ComponentKindsModel(dbs_global.Model):
    '''
    The model for storage kinds of components used in component model.
    Used to systematise components.
    '''
    __tablename__ = 'component_kinds'
    id_kind = dbs_global.Column(dbs_global.String(64), primary_key=True)
    description = dbs_global.Column(dbs_global.UnicodeText)

    @classmethod
    def find_by_id(
            cls, id_kind: str = None) -> 'ComponentKindsModel':
        # print(id_kind)
        return cls.query.filter_by(id_kind=id_kind).first()

    def update(self, update_values: Dict = None) -> None:
        if update_values is None:
            return
        for key in update_values.keys():
            setattr(self, key, update_values[key])
        self.save_to_db()

    def save_to_db(self) -> None:
        try:
            dbs_global.session.add(self)
            dbs_global.session.commit()
        except Exception as err:
            print('components.models.ComponentKindModel.save_to_db error\n', err)

    def delete_fm_db(self) -> None:
        try:
            dbs_global.session.delete(self)
            dbs_global.session.commit()
        except Exception as err:
            print('components.models.ComponentKindModel.delete_fm_db error\n', err)
