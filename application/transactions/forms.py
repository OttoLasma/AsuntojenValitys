from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class TransactionForm(FlaskForm):
    name = StringField("Task name", [validators.Length(min=2)])
    
 
    class Meta:
        csrf = False