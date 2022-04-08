from flask import Flask,render_template
from datetime import date

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
    return render_template("contact.html",now=x,title="contact")

if __name__=='__main__':
    app.run(debug=True)
    