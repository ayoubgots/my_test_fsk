from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def d():
    return render_template("home.html")


@app.route('/home')
def index():
    return render_template("home.html")


@app.route('/about')
def home():
    return render_template("about.html")

@app.route('/contact')
def k():
    return render_template("contact.html")

if __name__=='__main__':
    app.run(debug=True)
    