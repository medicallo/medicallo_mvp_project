from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app


from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app



class Doctor:
    db_name ="doc"
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data ['first_name']
        self.last_name=data['last_name']
        self.photo=data['photo']
        self.speciality=data['speciality']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.hospital_id=data['hospital_id']
        self.admin_id=data['admin_id']



# CREAT
    @classmethod
    def create_doctor(cls,data):
        query = "INSERT INTO doctors (first_name,last_name,photo,speciality,hospital_id) VALUES (%(first_name)s,%(last_name)s,%(photo)s,%(speciality)s,%(hospital_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)



# Read
    @classmethod
    def get_all(cls):
        query="SELECT * FROM doctors;"
        results=connectToMySQL(cls.db_name).query_db(query)
        doctors=[]
        for row in results:
            doctors.append(cls(row))
        return doctors

        
    @classmethod
    def get_one_by_id(cls,data):
        query="SELECT * FROM doctors WHERE id = %(id)s ;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(result[0])

# UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE doctors SET first_name=%(first_name)s, last_name=%(last_name)s, photo=%(photo)s, speciality=%(speciality)s, hospital_id=%(hospital_id)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
# DELETE
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM doctors WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
