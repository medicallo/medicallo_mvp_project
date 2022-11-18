from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app



class Category:
    db_name ="doc"
    def __init__(self,data):
        self.id=data['id']
        self.name=data ['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.card_id=data['card_id']
        self.admin_id=data['admin_id']


# CREAT
    @classmethod
    def create_category(cls,data):
        query = "INSERT INTO categories (name, card_id) VALUES (%(name)s,%(card_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)


# Read
    @classmethod
    def get_all_categories(cls):
        query="SELECT * FROM categories;"
        results=connectToMySQL(cls.db_name).query_db(query)
        users=[]
        for row in results:
            users.append(cls(row))
        return users

        
    @classmethod
    def get_category_by_card_id(cls,data):
        query="SELECT * FROM categories WHERE card_id = %(card_id)s ;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        print('*'*50,'hello',result)
        return result

    @classmethod
    def get_category_by_id(cls,data):
        query="SELECT * FROM categories WHERE id = %(id)s ;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result[0]

# UPDATE
    @classmethod
    def update_category(cls, data):
        query = "UPDATE categories SET name=%(name)s, card_id=%(card_id)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
# DELETE
    @classmethod
    def destroy_category(cls,data):
        query = "DELETE FROM categories WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
