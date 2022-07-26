
from cgitb import html
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, activity
from flask_app.models.user import User

# CREATE - ROUTES

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
        return redirect('/new/activity')
    else:
        activity.Activity.save(request.form)
        return redirect('/users/dashboard')

# READ - ROUTES

@app.route('/activity/<int:id>')
def show_activity(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("show_activity.html", workout=activity.Activity.get_one(data), user=User.get_by_id(user_data))

@app.route('/journal/<int:id>')
def show_journal(id):
    if 'user_id' not in session:
        return redirect('/')
    the_journal= activity.Activity.get_all({"user_id":session['user_id']})
    this_user = user.User.get_user_by_id(session['user_id'])
    this_activity = activity.Activity.get_one_activity(id)
    return render_template("user_activities.html", the_journal=the_journal, this_user=this_user, this_activity=this_activity)

# UPDATE - ROUTES

@app.route('/edit/activity/<int:id>')
def show_edit_activity_form(id):
    if 'user_id' not in session:
        return redirect('/')
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
        return redirect('/')
    if not activity.Activity.validate_activity(request.form):
        return redirect('/new/activity')
    data = {
        "activity_name": request.form["activity_name"],
        "id": request.form["id"]
    }
    activity.Activity.update_activity(data)
    return redirect('/users/dashboard')


# DELETE - ROUTES

@app.route('/destroy/activity/<int:id>')
def destroy_activity(id):
    if 'user_id' not in session:
        return redirect('/')
    activity.Activity.destroy(id)
    return redirect("/users/dashboard")