from flask_app.config.mysqlconnection import MySQLConnection,connectToMySQL
from flask_app import app
from flask import flash,session
from flask_app.models import user



class Goal:
    DB='group_project'

    def __init__(self, data):
        self.id = data['id']
        self.goal_name=data['goal_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id=data['user_id']

    # READ____MODEL____SQL

    @classmethod
    def get_all_user_goals(cls, data):
        query = """
        SELECT *
        FROM goals
        WHERE user_id = %(user_id)s
        ;"""
        goals_from_db = connectToMySQL(cls.DB).query_db(query, data)
        goals = []
        if not goals_from_db:
            return goals_from_db
        for goal in goals_from_db:
            goals.append(cls(goal))
        return goals

    @classmethod
    def get_goal_by_id(cls, data):
        query = """
        SELECT *
        FROM goals
        WHERE id = %(id)s
        ;"""
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])

    # @classmethod
    # def get_goal_with_activities(cls):
    #     query = """
    #     SELECT *
    #     FROM goals
    #     LEFT JOIN activities on goals.user_id = activities.user_id
    #     ;"""
    #     result = connectToMySQL(cls.db).query_db(query)
    #     # print("^^^^^^^^^^^^^^^^^^^^^", result)
    #     restaurants = []
    #     if not result:
    #         return result
    #     for row in result:
    #         new_restaurant = cls(row)
    #         this_diner = {
    #             'id': row['users.id'],
    #             'first_name': row['first_name'],
    #             'last_name': row['last_name'],
    #             'email': row['email'],
    #             'password': row['password'],
    #             'created_at': row['users.created_at'],
    #             'updated_at': row['users.updated_at'],
    #         }
    #         new_restaurant.diner = user.User(this_diner)
    #         restaurants.append(new_restaurant)
    #     print('****^^*(&&*(&&(&^&^*&^*^', restaurants)
    #     return restaurants



    #CREATE____MODEL____SQL

    @classmethod
    def add_goal(cls, data):
        if not cls.validate_goal_info(data):
            return False
        query = """
        INSERT INTO goals (goal_name, user_id) 
        VALUES (%(goal_name)s, %(user_id)s)
        ;"""
        goal_id = connectToMySQL(cls.DB).query_db(query,data)
        return goal_id



    #UPDATE____MODEL____SQL

    @classmethod
    def update_goal(cls, data):
        query = """UPDATE goals
        SET activity_name=%(goal_name)s, updated_at=NOW()
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.DB).query_db(query, data)



    #DELETE____MODEL____SQL







    #static method for VALIDATING 

    @staticmethod
    def validate_goal_info(goal):
        is_valid = True
        query = "SELECT * FROM goals WHERE id = %(id)s;"
        results = connectToMySQL(Goal.DB).query_db(query, goal)
        print(results)
        if not goal['goal_name']:
            flash("Name of goal must be least 3 characters.","create_goal")
            is_valid= False  
        return is_valid