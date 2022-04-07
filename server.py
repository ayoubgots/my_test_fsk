from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "this is my first app "


@app.route('/home')
def home():
    return "this is the page home "

@app.route('/ayoub')
def k():
    return "ayoubinat zwinanat "

if __name__=='__main__':
    app.run(debug=True)
    