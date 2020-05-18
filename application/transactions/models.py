from application import app, db
from application.models import Base

from sqlalchemy.sql import text


class Transaction(Base):
    currency = db.Column(db.String(144), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    
