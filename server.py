from socket import MsgFlag
from sqlite3 import dbapi2
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template,request
from datetime import date   
# from form import Registrationform,Loginfrom

x=date.today()
carte={}
row_byid=[]

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
def default():
    return render_template("home.html",now=x,title="home")


@app.route('/home')
def index():
    print(row_byid)
    return render_template("home.html",now=x,title="home",prods=laptop)
@app.route('/add/<id>')

def add(id):
    row=products.query.get(id)
    id=int(id)
    if( id not in carte.keys()):
        carte[id]=1
        row_byid.append(row)
    else:
        carte[id]+=1
    return render_template("panier.html",datarow=row_byid,carte=carte,prods=laptop)
 
    
@app.route('/remove/<int:id>')
def remove(id):
    row_byid.pop(id)
    print(row_byid)
    return render_template("panier.html",datarow=row_byid,carte=carte)
          
@app.route('/about')
def about():
    return render_template("about.html",now=x,title="about")

@app.route('/login')  
def contact():
    return render_template("login.html")

@app.route('/signup')
def login():
    return render_template('')


@app.route('/panier')
def panier():
    return render_template("panier.html",prod=laptop)
if __name__=='__main__':
    app.run(debug=True)
    