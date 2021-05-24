from flask_app.config.mysqlconnection import connectToMySQL

class Dojos:
    def __init__(self,data):
        self.id = data['id']
        self.fname = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        mysql = connectToMySQL("dojos_and_ninjas_schema")
        dojos = mysql.query_db("SELECT * FROM dojos;")
        print(dojos)
        return dojos
    
    @classmethod
    def add(cls,data):
        mysql = connectToMySQL("dojos_and_ninjas_schema")
        query="INSERT INTO dojos(name) VALUES(%(name)s);"
        new_dojo = mysql.query_db(query,data)
        return new_dojo

