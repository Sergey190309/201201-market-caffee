from uuid import uuid4
from time import time

from ..modules.dbs import dbs
from application.globals import GlobalConstants


class ConfirmationModel(dbs.Model):
    '''
    Used for user confirmations only.
    '''
    __tablename__ = 'confirmations'

    id = dbs.Column(dbs.String(50), primary_key=True)
    expire_at = dbs.Column(dbs.Integer, nullable=False)
    user_id = dbs.Column(dbs.Integer, dbs.ForeignKey('users.id'), nullable=False)
    confirmed = dbs.Column(dbs.Boolean, nullable=False, default=False)

    user = dbs.relationship(
        'UserModel',
        backref='usermodel'
        # lazy='dynamic',
        # cascade='all, delete-orphan'
    )

    def __init__(self, user_id: int, **kwargs):
        super().__init__(**kwargs)
        self.user_id = user_id
        self.id = uuid4().hex
        self.expire_at = \
            int(time()) + GlobalConstants.get_CONFIRMATION_EXPIRATION_DELTA
        self.confirmed = False

    @classmethod
    def find_by_id(cls, _id: str) -> "ConfirmationModel":
        return cls.query.filter_by(id=_id).first()

    @property
    def expired(self) -> bool:
        return time() > self.expire_at

    def force_to_expire(self) -> None:  # forcing current confirmation to expire
        if not self.expired:
            self.expire_at = int(time())
            self.save_to_db()

    def save_to_db(self) -> None:
        dbs.session.add(self)
        dbs.session.commit()

    def delete_from_db(self) -> None:
        dbs.session.delete(self)
        dbs.session.commit()
