from flask import Flask
from flask_wtf import  FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo



class Registrationform(FlaskForm):
    username=StringField('UserName:',validators=[DataRequired(),Length(min=1,max=20)])
    email=StringField('email:',validators=[DataRequired(),Email()])
    password=PasswordField('password:',validators=[DataRequired()])
    confirm_passowrd=PasswordField('confirm password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('sign up')
    
class Loginfrom(FlaskForm):
    email=StringField('email:',validators=[DataRequired(),Email()])
    password=PasswordField('password:',validators=[DataRequired()])
    confirm_passowrd=PasswordField('confirm password',validators=[DataRequired(),EqualTo('password')])
    remember=BooleanField("remember me ")
    submit=SubmitField('log in')
    