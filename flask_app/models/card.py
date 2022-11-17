from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app) 
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Card:
    db_name ="doc"
    def __init__(self,data):
        self.id=data['id']
        self.name=data ['name']
        self.photo=data['photo']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.admin_id=data['admin_id']

# CREATE
    @classmethod
    def create_card(cls,data):
        query = "INSERT INTO cards (name,photo) VALUES (%(name)s,%(photo)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)



# Read
    @classmethod
    def get_all(cls):
        query="SELECT * FROM cards;"
        results=connectToMySQL(cls.db_name).query_db(query)
        cards=[]
        for row in results:
            cards.append(cls(row))
        return cards


    @classmethod
    def get_card_by_id(cls,data):
        query="SELECT * FROM cards WHERE id = %(id)s ;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(result[0])


# UPDATE
    @classmethod
    def update_card(cls, data):
        query = "UPDATE cards SET name=%(name)s, photo=%(photo)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
# DELETE
    @classmethod
    def destroy_card(cls,data):
        query = "DELETE FROM cards WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
