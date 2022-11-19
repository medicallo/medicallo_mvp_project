from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Admin:
    db_name ="doc"
    def __init__(self,data):
        self.id=data['id']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    
    @classmethod
    def create_admin(cls,data):
        query = "INSERT INTO admin (email,password) VALUES (%(email)s, %(password)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    
    
    @classmethod
    def get_one_by_id(cls,data):
        query="SELECT * FROM admin WHERE id = %(id)s ;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(result[0])


    @classmethod
    def get_one_by_email(cls,data):
        query="SELECT * FROM admin WHERE email = %(email)s ;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])

    @staticmethod
    def validate_admin(data):
        is_valid = True # we assume this is true.
        query="SELECT * FROM admin WHERE email = %(email)s ;"
        result = connectToMySQL(Admin.db_name).query_db(query,data)
        if len(result)>=1:
            flash("Email Already Exist", 'email')
        if not EMAIL_REGEX.match(data['email']): 
            flash("Incorrect Email", 'email')
            is_valid = False
        if len(data['password']) < 3:
            flash("password must be at least 8 characters.", 'email')
            is_valid = False
        return is_valid


