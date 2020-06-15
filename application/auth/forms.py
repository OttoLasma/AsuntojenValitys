from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=2, max=144, message="Username has to be at least 2 characters and less than 144 characters"), validators.InputRequired(message='Field is required')])
    password = PasswordField("Password", [validators.Length(min=2, max=144, message="Password has to be at least 2 characters and less than 144 characters"), validators.InputRequired(message='Field is required')])

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name =  StringField('Name', [validators.Length(min=2, max=144, message="Valid name is longer than two characters :D"), validators.InputRequired(message='Field is required')])
    username = StringField('Username', [validators.Length(min=2, max=144, message="Username has to be at least 2 characters and less than 144 characters"), validators.InputRequired(message='Field is required')])
    password = PasswordField("Password", [validators.Length(min=3, max=20, message="Password has to be at least 2 characters and less than 144 characters"), validators.InputRequired(message='Field is required')])
