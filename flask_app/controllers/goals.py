from flask_app import app
from flask import render_template,redirect,request,session, flash
from flask_app.models import user,goal,activity

# CREATE - ROUTES

@app.route('/dashboard')
def show_goals():
    this_user = user.User.

