from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
# from flask import flash
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app) 
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    db_name ="doc"
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data ['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.admin_id=data['admin_id']
        self.users = 0
    @classmethod
    def create_user(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s, %(password)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_one_by_email(cls,data):
        query="SELECT * FROM users WHERE email = %(email)s ;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])

    @classmethod
    def get_one_by_id(cls,data):
        query="SELECT * FROM users WHERE id = %(id)s ;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_all(cls):
        query="SELECT * FROM users;"
        results=connectToMySQL(cls.db_name).query_db(query)
        users=[]
        for row in results:
            users.append(cls(row))
        return users

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


    @classmethod
    def get_user_with_show( cls , data ):
        query ="SELECT * FROM users LEFT JOIN shows ON shows.user_id = users.id WHERE users.id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db( query , data )
        # results will be a list of user objects with the burger attached to each row. 
        user = cls( results[0] )
        for row_from_db in results:
            # Now we parse the burger data to make instances of shows and add them into our list.
            show_data = {
                "id" : row_from_db["shows.id"],
                "title" : row_from_db["shows.title"],
                "network" : row_from_db['network'],
                "description" : row_from_db['description'],
                "date" : row_from_db['date'],
                "created_at" : row_from_db["shows.created_at"],
                "updated_at" : row_from_db["shows.updated_at"]
            }
            user.show.append( Show( show_data ) )
        return user
    