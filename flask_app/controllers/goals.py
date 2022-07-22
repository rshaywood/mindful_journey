from flask_app import app
from flask import render_template,redirect,request,session, flash
from flask_app.models import user,goal,activity

# CREATE - ROUTES

@app.route('/dashboard')
def show_goals():
    user_goals = goal.Goal.get_all_user_goals({"user_id":session['user_id']})
    this_user = user.User.get_user_by_id(session['user_id'])
    return render_template('dashboard.html', this_user=this_user, user_goals=user_goals)



