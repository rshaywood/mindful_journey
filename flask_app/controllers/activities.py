
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, activity
from flask_app.models.user import User


@app.route('/new/activity')
def new_activity():
    if 'user_id' not in session:
        return redirect('/logout')
   # data = {
       # "id": session['user_id']
    # }
    return render_template('add_activity.html')


@app.route('/create/activity', methods=['POST'])
def create_activity():
    if 'user_id' not in session:
        return redirect('/logout')
    if not activity.Activity.validate_activity(request.form):
        return redirect('/add/activity')
    # data = {
    #     "activity_name": request.form["activity_name"],
    #     "user_id": session["user_id"]
    # }
    activity.Activity.save(request.form)
    return redirect('/dashboard')


@app.route('/edit/activity/<int:id>')
def edit_activity(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("edit_activity.html", edit=activity.Activity.get_one(data), user=User.get_by_id(user_data))


@app.route('/update/activity', methods=['POST'])
def update_activity():
    if 'user_id' not in session:
        return redirect('/logout')
    if not activity.Activity.validate_workout(request.form):
        return redirect('/new/activity')
    data = {
        "activity_name": request.form["activity_name"],
        "id": request.form["id"]
    }
    activity.Activity.update(data)
    return redirect('/dashboard')


@app.route('/activity/<int:id>')
def show_activity(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("show_activity.html", workout=activity.Activity.get_one(data), user=User.get_by_id(user_data))


@app.route('/destroy/activity/<int:id>')
def destroy_activity(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    activity.Activity.destroy(data)
    return redirect('/dashboard')
