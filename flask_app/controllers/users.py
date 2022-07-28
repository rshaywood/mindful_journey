
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, activity
import os
# these two lines for uploading image for user to db and retrieve it as well
from werkzeug.utils import secure_filename


# home page route
@app.route("/")
def home():
    # for showing user's image in main page
    # data={
    #         'id':session['user_id']
    # }
    # this_user = user.User.get_user_by_id(data)
    return render_template('home.html')

# create user


@app.route('/signup')
def page_to_register_user():
    return render_template("signup.html")


@app.route("/create/user", methods=["POST"])
def register_user():
    if('user_image' not in request.files or request.files['user_image'].filename == ""):
        flash("You Must upload an image")
        return redirect("/signup")
    image = request.files['user_image']
    filename = secure_filename(image.filename)
    print(filename)
    print(app.config["UPLOAD_FOLDER"])
    image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": request.form['password'],
        "confirm_password": request.form['confirm_password'],
        "user_image": os.path.join("/static/images", filename),
    }
    print("^^^^^^^^^", data)
    if user.User.create_user(data):
        return redirect('/users/dashboard')
    else:
        return redirect("/signup")


# login routes to get user to dashboard
@app.route('/login')
def page_to_login_user():
    return render_template("login.html")


@app.route("/users/login", methods=['POST'])
def login():
    if user.User.login(request.form):
        return redirect("/users/dashboard")
    return redirect('/login')

# route for login/registration to take to dashboard


@app.route("/users/dashboard")
def user_dashboard():
    # this for retreiving user's imag from db //go to dashboard and check     <img src="{{this_user.user_image}}" alt="" class="user_image">
    # activities= activity.Activity.get_all({"user_id":session['user_id']})
    latest_activity = activity.Activity.get_latest_activity({"user_id":session['user_id']})
    this_user = user.User.get_user_by_id(session['user_id'])
    return render_template("dashboard.html", this_user=this_user, latest_activity=latest_activity)


@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')