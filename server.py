from socket import MsgFlag
from sqlite3 import dbapi2
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template,request
from datetime import date
import sqlalchemy

# from form import Registrationform,Loginfrom

x=date.today()

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///mystore.db'
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
    
    
laptop=products.query.all()

@app.route('/')
def d():
    return render_template("home.html",now=x,title="home")


# @app.route('/home')
# def index():
#     return render_template("home.html",now=x,title="home",prods=laptop)


@app.route('/about')
def home():
    return render_template("about.html",now=x,title="about")

@app.route('/contact')
def k():
    name=request.form.get("name")
    email=request.form.get("email")
    message=request.form.get("message")
    msg={'name':name,'email':email,'message':message}
    return render_template("contact.html",now=x,title="contact")

@app.route('/signup')
def login():
    return render_template('')
# @app.route('/panier')
# def panier():
#     return render_template("panier.html")
if __name__=='__main__':
    app.run(debug=True)
    