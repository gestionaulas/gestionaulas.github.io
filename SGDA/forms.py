from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from pymongo import MongoClient


class RegistrationForm(FlaskForm):
    email = StringField('email',  validators=[DataRequired(), Length(max=30)])
    password = PasswordField('password', validators=[DataRequired()])
    username = StringField('Username', validators = [DataRequired(), Length(min=6,max=12)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
