from application import app, db
from application.models import Base
from flask_login import current_user
from sqlalchemy.sql import text
import json


class Transaction(Base):
    currency = db.Column(db.String(144), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    @staticmethod  
    def get_transactions():
        return Transaction.query.filter_by(account_id = current_user.id)