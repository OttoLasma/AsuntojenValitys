from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class TransactionForm(FlaskForm):
    name = StringField("Task name", [validators.Length(min=2)])
    done = BooleanField("Done")
 
    class Meta:
        csrf = False