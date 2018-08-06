from flask import render_template
from halo import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")