import email
from flask import Flask
from flask_wtf import  FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,EmailField
from wtforms.validators import DataRequired,Length,Email,EqualTo




class Registrationform(FlaskForm):
    username=StringField('UserName',validators=[DataRequired(),Length(min=2,max=20)])
    password=PasswordField('password',validators=[DataRequired()])
    confirm_passowrd=PasswordField('confirm password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('sign up')
    
class Loginfrom(FlaskForm):
    username=StringField('UserName',validators=[DataRequired(),Length(min=1,max=20)])
    password=PasswordField('password',validators=[DataRequired()])
    remember=BooleanField("remember")
    submit=SubmitField('log in')
    