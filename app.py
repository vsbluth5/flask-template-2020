# ---- BIRTHSTONE APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', mychoice="")
    
@app.route('/result', methods=['GET', 'POST'])
def birthstone():
    if request.method == 'GET':
        return "You need to post a month using the radiobuttons!"
    else:
        choice = dict(request.form)
        # print(choice)
        proprts = model.findMonth(choice)
        
        return render_template('results.html', props=proprts)
       # return render_template('results.html', month=mon, source=source, birthstone=bstone)
