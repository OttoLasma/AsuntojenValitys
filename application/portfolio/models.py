from application import app, db
from application.models import Base
from flask_login import current_user
from sqlalchemy.sql import text




class Portfolio(Base):
    
    btc_amount = db.Column(db.Integer, nullable=True)
    eth_amount = db.Column(db.Integer, nullable=True)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    def __init__(self, account_id, btc_amount, eth_amount):
        self.btc_amount = btc_amount
        self.eth_amount = eth_amount
        self.account_id = account_id
        