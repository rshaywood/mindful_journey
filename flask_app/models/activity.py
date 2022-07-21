from flask_app.config.mysqlconnection import MySQLConnection,connectToMySQL
from flask_app import app
from flask import flash,session
from flask_app.models import user



class Activity:
    DB = 'group_project'

    def __init__(self, data):
        self.id = data['id']
        self.activity_name = data['activity_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.creator = None  # this for create instance of user

    # #READ____MODEL____SQL

    @classmethod
    def save(cls, data):
        query = """INSERT INTO activities (activity_name, user_id) 
        VALUES (%(activity_name)s,%(user_id)s);"""
        return connectToMySQL(cls.DB).query_db(query, data)

    # CREATE____MODEL____SQL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM activities;"
        results = connectToMySQL(cls.DB).query_db(query)
        Activities = []
        for row in results:
            print(row['activity_name'])
            Activities.append(cls(row))
        return Activities

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM activities WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    # UPDATE____MODEL____SQL

    @classmethod
    def update(cls, data):
        query = """UPDATE activities SET activity_name=%(activity_name)s, updated_at=NOW() WHERE id = %(id)s;"""
        return connectToMySQL(cls.DB).query_db(query, data)

    # DELETE____MODEL____SQL

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM activities WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)

    # static method for VALIDATEING

    @staticmethod
    def validate_activity(activity):
        is_valid = True
        if len(activity['activity_name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters", "activity")
        return is_valid
