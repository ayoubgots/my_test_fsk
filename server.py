
from socket import MsgFlag
from sqlite3 import dbapi2
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template,request
from datetime import date
import sqlalchemy


x=date.today()

laptop=[
    {
        "titre" :"hwawei",
        "image" :"hwawei.png",
        "description" :"blabalbalabl"    
    },
    {
        "titre" :"samsung",
        "image" :"samsung.png",
        "description" :"lahawla"    
    },
    {
        "titre" :"mac",
        "image" :"mac.png",
        "description" :"mac ya khouya"    
    }, 
    {
        "titre" :"ayoub",
        "image" :"mac.png",
        "description" :"mac ya khouya"    
    }, 
    {
        "titre" :"ayoub",
        "image" :"mac.png",
        "description" :"mac ya khouya"    
    }, 
    {
        "titre" :"ayoub",
        "image" :"mac.png",
        "description" :"mac ya khouya"    
    }, 
    {
        "titre" :"ayoub",
        "image" :"mac.png",
        "description" :"mac ya khouya"    
    }, 
    {
        "titre" :"ayoub",
        "image" :"mac.png",
        "description" :"mac ya khouya"    
    }, 
    
]




app = Flask(__name__)

messages=[]

app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db=SQLAlchemy(app)

class products(db.Model):
    id=db.Column(db.Integer ,primary_key=True)
    titre=db.Column(db.String(20),nullable=False)
    description=db.Column(db.Text,nullable=False)
    prix=db.Column(db.Integer,nullable=False)
    image=db.Column(db.String(20),nullable=False)

class Message(db.Model):
    id=db.Column(db.Integer ,primary_key=True)
    nom=db.Column(db.String(20),nullable=False)
    message=db.Column(db.Text,nullable=False)
    mail=db.Column(db.String(20),nullable=False)
    

@app.route('/')
def d():
    return render_template("home.html",now=x,title="home")


@app.route('/home')
def index():
    return render_template("home.html",now=x,title="home",prods=laptop)


@app.route('/about')
def home():
    return render_template("about.html",now=x,title="about")

@app.route('/contact')
def k():
    name=request.form.get("name")
    email=request.form.get("email")
    message=request.form.get("message")
    msg={'name':name,'email':email,'message':message}
    messages.append(msg)
    print(messages)
    return render_template("contact.html",now=x,title="contact")

if __name__=='__main__':
    app.run(debug=True)
    