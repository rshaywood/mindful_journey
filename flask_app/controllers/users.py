
from flask_app import app
from flask import render_template,redirect,request,session, flash
from flask_app.models import user,goal,activity


# home page route
@app.route("/")
def home():
    return render_template('home.html')

#create user
@app.route('/register')
def page_to_register_user():
    return render_template("register.html")

@app.route("/create/user", methods=["POST"])
def register_user():
    if user.User.create_user(request.form):
        return redirect('/users/dashboard')
    return redirect ("/register")



