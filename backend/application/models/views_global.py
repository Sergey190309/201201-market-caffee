from typing import Dict, List
from application.modules.dbs_global import dbs_global


class ViewGlobalModel(dbs_global.Model):
    '''
    The model for storage site contents views. Used to systematise contents table.

    '''
    __tablename__ = 'views_global'
    id_view = dbs_global.Column(dbs_global.String(64), primary_key=True)
    description = dbs_global.Column(dbs_global.UnicodeText)

    @classmethod
    def find(cls, searching_criterions: Dict = {})\
            -> List['ViewGlobalModel']:
        return cls.query.filter_by(**searching_criterions).all()

    @classmethod
    def find_by_id(cls, id_view: str = None) -> 'ViewGlobalModel':
        # print(id_view)
        return cls.query.filter_by(id_view=id_view).first()

    def update(self, update_values: Dict = None) -> None:
        if update_values is None:
            return
        for key in update_values.keys():
            setattr(self, key, update_values[key])
        self.save_to_db()

    def is_exist(self):
        return ViewGlobalModel.find_by_id(self.id_view) is not None

    def save_to_db(self) -> None:
        try:
            dbs_global.session.add(self)
            dbs_global.session.commit()
        except Exception as err:
            print('contents.models.ViewsModel.save_to_db error\n', err)

    def delete_fm_db(self) -> None:
        # print('\nViewGlobalModel, delete_fm_db ->')
        try:
            dbs_global.session.delete(self)
            dbs_global.session.commit()
        except Exception as err:
            print('contents.models.ViewsModel.delete_fm_db error\n', err)
