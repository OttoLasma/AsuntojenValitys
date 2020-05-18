from application import db
from application.models import Base

from sqlalchemy.sql import text


class Portfolio(Base):
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    BTC_amount = db.Column(db.Integer, nullable=True)
    BTC_amount = db.Column(db.Integer, nullable=True)

    def __init__(self, BT, BTC_amount):
        self.name = name
        self.BTC_amount = BTC_amount
        