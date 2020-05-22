from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, IntegerField, ValidationError

def valid_currency(form, field):
    list = ["ETH", "BTC", "LINK" , "XRP"]
    if field.data not in list:
        raise ValidationError('This particular currency has not been identified by the platform')
    
class TransactionForm(FlaskForm):
    currency = StringField('Currency', [validators.Length(min=3, max=5, message="Please use the abbreviation of the currency in question"), valid_currency])
    amount = IntegerField("Amount", [validators.NumberRange(min=None, max=None, message="Value must be an integer")])
    class Meta:
        csrf = False
        
class TransactionEditForm(FlaskForm):
    currency = StringField('Currency', [validators.Length(min=3, max=5, message="Please use the abbreviation of the currency in question"), valid_currency])
    amount = IntegerField("Amount", [validators.NumberRange(min=None, max=None, message="Value must be an integer")])
    class Meta:
        csrf = False