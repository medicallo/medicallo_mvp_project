from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Admin:
    db_name ="black"
    def __init__(self,data):
        self.id=data['id']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @staticmethod
    def validate_user(data):
        is_valid = True # we assume this is true.
        query="SELECT * FROM users WHERE email = %(email)s ;"
        result = connectToMySQL(User.db_name).query_db(query,data)
        if len(result)>=1:
            flash("Email Already Exist", 'email')
        if not EMAIL_REGEX.match(data['email']): 
            flash("Incorrect Email", 'email')
            is_valid = False
        if len(data['first_name']) < 2:
            flash("first Name must be at least 2 characters.",'email' )
            is_valid = False
        if len(data['last_name']) < 2:
            flash("last name must be at least 2 characters.", 'email')
            is_valid = False
        if len(data['password']) < 3:
            flash("password must be at least 8 characters.", 'email')
            is_valid = False
        if data['password']!=data ['confirm_password'] :
            flash("password Don't match.", 'email')
            is_valid = False
        return is_valid


