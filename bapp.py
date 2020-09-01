# ---- TEMPLATE YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
# from flask import request


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    props = {
        'title': 'Home',
        'first_name': 'Alejandra'
    }
    return render_template('index.html', props=props)




# def index():
#     # return "<h1>hello world</h1>"
#     return render_template('index.html')

@app.route('/secret')
def secret():
    return "<h1>You found the secret!</h1>"

