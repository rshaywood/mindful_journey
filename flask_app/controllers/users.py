
from flask_app import app
from flask import render_template,redirect,request,session, flash
from flask_app.models import user,goal,activity


# home page route
@app.route("/")
def home():
    return render_template('home.html')



