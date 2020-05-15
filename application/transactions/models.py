from application import db
from application.models import Base

class Transaction(db.Model):
    

    name = db.Column(db.String(144), nullable=False)
    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    def __init__(self, name):
        self.name = name
        # self.done = False