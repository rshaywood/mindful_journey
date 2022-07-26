from flask_app.config.mysqlconnection import MySQLConnection,connectToMySQL
from flask_app import app
from flask import flash,session
from flask_app.models import user



class Activity:
    DB = 'group_project'

    def __init__(self, data):
        self.id = data['id']
        self.goal_name = data['goal_name']
        self.activity_name = data['activity_name']
        self.comment = data['comment']
        self.feeling_before = data['feeling_before']
        self.feeling_after = data['feeling_after']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        # self.creator = None  # this for create instance of user

# #READ____MODEL____SQL

    @classmethod
    def save(cls, data):
        query = """INSERT INTO activities (goal_name,activity_name,comment,feeling_before,user_id) 
        VALUES (%(goal_name)s,%(activity_name)s,%(comment)s,%(feeling_before)s,%(user_id)s);"""
        result=connectToMySQL(cls.DB).query_db(query, data)
        print("%%%%%%%%%%%%%%%",result)
        return result

    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM activities WHERE user_id=%(user_id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        activities = []
        for row in results:
            # print("*******************", row)
            activities.append(row)
        return activities


    @classmethod
    def get_one_activity(cls, data):
        query = "SELECT * FROM activities WHERE id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        if result:
            result = (result[0]) 
        return result

    @classmethod
    def get_one_goal(cls, data):
        query = "SELECT goal_name FROM activities WHERE id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])

    # CREATE____MODEL____SQL


    # UPDATE____MODEL____SQL

    @classmethod
    def update_activity(cls, data):
        query = """UPDATE activities SET goal_name=%(goal_name)s,activity_name=%(activity_name)s,comment=%(comment)s,feeling_before=%(feeling_before)s WHERE id = %(id)s;"""
        return connectToMySQL(cls.DB).query_db(query, data)

    # DELETE____MODEL____SQL

    @classmethod
    def destroy(cls, id):
        data = {"id" : id}
        query = """
        DELETE FROM activities 
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.DB).query_db(query, data)

    # static method for VALIDATEING

    @staticmethod
    def validate_activity(activity):
        is_valid = True
        if len(activity['activity_name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters", "activity")
        if not (activity['goal_name']) :
            is_valid = False
            flash("You must choose a goal")
        if not (activity['comment']) :
            is_valid = False
            flash("Comment must be at least 3 characters ")
        return is_valid
