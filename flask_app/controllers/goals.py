from flask_app import app
from flask import render_template,redirect,request,session, flash
from flask_app.models import user,goal,activity

# CREATE - ROUTES

@app.route('/dashboard')
def show_goals():
    user_goal = goal.Goal.get_goal_by_id({"user_id":session['user_id']})
    this_user = user.User.get_user_by_id(session['user_id'])
    return render_template('dashboard.html', this_user=this_user, user_goal=user_goal)



