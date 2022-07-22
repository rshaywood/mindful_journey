
from flask_app import app
from flask import render_template,redirect,request,session, flash
from flask_app.models import user,goal,activity


# home page route
@app.route("/")
def home():
    return render_template('home.html')

#create user
@app.route('/signup')
def page_to_register_user():
    return render_template("signup.html")

@app.route("/create/user", methods=["POST"])
def register_user():
    if user.User.create_user(request.form):
        return redirect('/users/dashboard')
    return redirect ("/signup")

#login routes to get user to dashboard
@app.route('/login')
def page_to_login_user():
    return render_template("login.html")

@app.route("/users/login", methods=['POST'])
def login(): 
    if user.User.login(request.form): 
        return redirect("/users/dashboard")
    return redirect('/')

#route for login/registration to take to dashboard
@app.route("/users/dashboard")
def user_dashboard():
    return render_template("dashboard.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')
