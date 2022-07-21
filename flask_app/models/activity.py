from flask_app.config.mysqlconnection import MySQLConnection,connectToMySQL
from flask_app import app
from flask import flash,session
from flask_app.models import user



class Activity:
    DB='group_project'

    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id=data['user_id']
        self.creator=None#this for create instance of user

    # #READ____MODEL____SQL





    #CREATE____MODEL____SQL





    #UPDATE____MODEL____SQL





    #DELETE____MODEL____SQL







    #static method for VALIDATEING 