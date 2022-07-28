
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, activity
from flask_app.models.user import User

# CREATE - ROUTES


@app.route('/new/activity')
def new_activity():
    if 'user_id' not in session:
        return redirect('/')
   # data = {
       # "id": session['user_id']
    # }
    return render_template('add_activity.html')


@app.route('/create/activity', methods=['POST'])
def create_activity():
    if 'user_id' not in session:
        return redirect('/')
    if not activity.Activity.validate_activity(request.form):
        return redirect('/new/activity')
    else:
        activity.Activity.save(request.form)
        return redirect(f"/journal/{session['user_id']}")

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
    data={
        'id':session['user_id']
        }
    # the_journal = activity.Activity.get_all({"user_id": session['user_id']})
    the_journal=user.User.get_activities_by_this_user(data)
    this_user = user.User.get_user_by_id(session['user_id'])
    # this_activity = activity.Activity.get_one_activity(id)
    return render_template("user_activities.html", the_journal=the_journal, this_user=this_user)

# UPDATE - ROUTES


@app.route('/edit/activity/<int:id>')
def show_edit_activity_form(id):
    if 'user_id' not in session:
        return redirect('/')
    # data = {
    #     "id": id
    # }
    user_data = {
        "id": session['user_id']
    }
    return render_template("edit_activity.html", edit=activity.Activity.get_one_activity(id), user=User.get_user_by_id(user_data))


@app.route('/edit/activity/<int:id>', methods=['POST'])
def edit_activity(id):
    if 'user_id' not in session:
        return redirect('/')
    if not activity.Activity.validate_activity(request.form):
        edit=activity.Activity.get_one_activity(id)
        return render_template('edit_activity.html',edit=edit)
    # edit_activity=activity.Activity.get_one_activity(id)
    activity_data = {
        'id':id,
        "goal_name": request.form["goal_name"],
        "activity_name": request.form["activity_name"],
        "comment": request.form["comment"],
        "feeling_before": request.form["feeling_before"],
        "feeling_after": request.form["feeling_after"]
    }
    if(activity.Activity.update_activity(activity_data)==None):
        return redirect(f"/journal/{id}")
    else:
        return redirect('/users/dashboard')



# DELETE - ROUTES

@app.route('/destroy/activity/<int:id>')
def destroy_activity(id):
    if 'user_id' not in session:
        return redirect('/')
    activity.Activity.destroy(id)
    return redirect(f"/journal/{id}")
