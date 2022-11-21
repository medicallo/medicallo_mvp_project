from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app




class Hospital:
    db_name ="doc"
    def __init__(self,data):
        self.id=data['id']
        self.name=data ['name']
        self.photo=data['photo']
        self.location=data['location']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.admin_id=data['admin_id']



# CREATE
    @classmethod
    def create_hospital(cls,data):
        query = "INSERT INTO hospitals (name,photo,location) VALUES (%(name)s,%(photo)s,%(location)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)



# Read
    @classmethod
    def get_all_hospital(cls):
        query="SELECT * FROM hospitals;"
        results=connectToMySQL(cls.db_name).query_db(query)
        hospitals=[]
        for row in results:
            hospitals.append(cls(row))
        return hospitals

        
    @classmethod
    def get_hospital_by_id(cls,data):
        query="SELECT * FROM hospitals WHERE id = %(id)s ;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result[0]

# UPDATE
    @classmethod
    def update_hospital(cls, data):
        query = "UPDATE hospitals SET name=%(name)s, photo=%(photo)s, location=%(location)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
# DELETE
    @classmethod
    def destroy_hospital(cls,data):
        query = "DELETE FROM hospitals WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

# JOIN 3 Tables
    @classmethod
    def get_hospital_with_doc_disease(cls,data):
        query= "SELECT diseases.id ,diseases.name FROM hospitals join doctors on doctors.hospital_id=hospitals.id join diseases on diseases.doctor_id=doctors.id join categories on categories.id=diseases.category_id where hospitals.id=%(hos_id)s and categories.id =%(cat_id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
