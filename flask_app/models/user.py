
from flask_app.config.mysqlconnection import MySQLConnection,connectToMySQL
from flask_app import app
from flask_app.models import activity,goal
from flask import flash,session
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) 



class User:
    DB='group_project'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password=data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.activites=[]

#CREATE ----SQL----MODELS
    @classmethod 
    def create_user(cls, data):
        if not cls.validate_user_reg_data(data):
            return False
        else:
            data = cls.parse_registration_data(data)
            query = """
            INSERT INTO users 
            (first_name, last_name, email, password)
            VALUES
            (%(first_name)s, %(last_name)s, %(email)s, %(password)s)
            ;"""
            user_id = connectToMySQL(cls.db).query_db(query,data)
            session["user_id"] = user_id
            return user_id

#READ ----SQL----MODELS

    @classmethod
    def get_user_by_id(cls, id):
        data = {'id' : id}
        query = """
        SELECT * FROM users
        WHERE id = %(id)s
        ;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        if result:
            result = cls(result[0])
        return result

    @classmethod
    def get_user_by_email(cls, email):
        data = {'email' : email}
        query = """
        SELECT * FROM users
        WHERE email = %(email)s
        ;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        if result:
            result = cls(result[0])
        return result


#UPDATE ----SQL----MODELS


#DELETE ----SQL----MODELS








#static method for valdiation USER

    @staticmethod
    def validate_user_reg_data(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #this regulaer exp for making sure the email must have charecters like letters and @ nd dot ...etc
        is_valid = True # we assume this is true
        #validate our email to see if its in correct format
        if not EMAIL_REGEX.match(data['email']):
            flash("Use a real email")
            is_valid=False
        # now after creating get _user_by_email method will call it here if the result came true.
        if User.get_user_by_email(data['email'].lower()):#lower function here for preventing duplicate emails if we insert by mistake uppercase and lower case , so in this case all leteeres will converted to uppercase.
            flash("Email already in use, insert another email adress")
            is_valid=False
        #validat first_name to make sure it is more than 3 chareters
        if len(data['first_name']) < 3:
            flash("first_Name must be at least 3 or more characters.")
            is_valid = False
        #validata last_name to make sure it is 3 charecters or more than 3 chareters
        if len(data['last_name']) < 3:
            flash("last_name must be at least 3 or more characters.")
            is_valid = False
        #validate password to make sure its more than 8 charecters
        if len(data['password'])<8:
            flash("your password must contain at least 8 charecters")
            is_valid=False
        #validate password again to make sure it matches the confirm password
        if data['password']!=data['confirm_password']:
            flash("password do not match")
            is_valid=False
        return is_valid


#static method for parsed data to hashed our password (the data coming from form are plain as we inserted and to hash the password before passing it to db ,we need to hash it so, it will appear as a random charecters in db , to do so will create pased function with parsed empty dictionary like below:)
    @staticmethod
    def parse_regestration_data(data):
        parsed_data={}
        parsed_data['email']=data['email'].lower()#the data I give you find the key and set its value
        parsed_data['password']=bcrypt.generate_password_hash(data['password'])
        parsed_data['first_name']=data['first_name']
        parsed_data['last_name']=data['last_name']
        return parsed_data
        #now we have to go to top and call this function to hash password before creating user
        
    #method for login
    @staticmethod
    def login(data):
        # will check if the email came from db so we will check if the password matches 
        user=User.get_user_by_email(data['email'].lower())
        if user :
            if bcrypt.check_password_hash(user.password,data['password']):
                session['user_id']=user.id#store the user id that came with email into session
                session['first_name']=user.first_name
                session['last_name']=user.last_name#we stored both first and last name in session so in this case when go to dashboard or edit page , we do not need to calll get user by id and pass it with render template to display it on the screen.
                return True
        #if no thing back from method get_user_by_email:
        flash("invalid email adress or password")
        return False

