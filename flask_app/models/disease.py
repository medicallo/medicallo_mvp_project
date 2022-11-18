from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app



class Disease:
    db_name ="doc"
    def __init__(self,data):
        self.id=data['id']
        self.name=data ['name']
        self.comment=data ['comment']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.doctor_id=data['doctor_id']
        self.category_id=data['category_id']
        self.admin_id=data['admin_id']


# CREAT
    @classmethod
    def create_disease(cls,data):
        query = "INSERT INTO diseases (name,comment,doctor_id,category_id) VALUES (%(name)s,%(comment)s,%(doctor_id)s, %(category_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)



# Read
    @classmethod
    def get_all_diseases(cls):
        query="SELECT * FROM diseases;"
        results=connectToMySQL(cls.db_name).query_db(query)
        diseases=[]
        for row in results:
            diseases.append(cls(row))
        return diseases

        
    @classmethod
    def get_disease_by_id(cls,data):
        query="SELECT * FROM diseases WHERE category_id = %(category_id)s AND doctor_id = %(doctor_id)s  ;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(result[0])

# UPDATE
    @classmethod
    def update_disease(cls, data):
        query = "UPDATE diseases SET name=%(name)s, comment=%(comment)s, doctor_id=%(doctor_id)s, category_id=%(category_id)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
# DELETE
    @classmethod
    def destroy_disease(cls,data):
        query = "DELETE FROM diseases WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
