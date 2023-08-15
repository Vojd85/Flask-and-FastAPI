# WTForms

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo




class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_pas = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
