from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Admin:
    db_name ="doc"
    def __init__(self,data,id=2):
        self.id=id
        self.email=data['email']
        self.password=data['password']


    
    @classmethod
    def get_admin_by_id(cls,data):
        query="SELECT * FROM admin WHERE id = %(id)s ;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result[0]


    @classmethod
    def get_admin_by_email(cls,data):
        query="SELECT * FROM admin WHERE email = %(email)s ;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        if len(result)<1:
            return False
        return result[0]



