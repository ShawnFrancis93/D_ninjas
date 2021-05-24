from flask_app.config.mysqlconnection import connectToMySQL
class Ninjas:
    def __init__(self,data):
        self.id = data['id']
        self.fname = data['first_name']
        self.lname = data['last_name']
        self.age=data['age']
        self.dojo=data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all_in_x(cls,id):
        mysql = connectToMySQL("dojos_and_ninjas_schema")
        query=("SELECT * FROM dojos JOIN ninjas ON dojos.id=ninjas.dojos_id WHERE dojos.id = %(id)s ;")
        all_ninjas = mysql.query_db(query,id)
        print(all_ninjas)
        return all_ninjas

    @classmethod
    def add_ninjas(cls,data):
        mysql = connectToMySQL("dojos_and_ninjas_schema")
        query=("INSERT INTO ninjas(first_name,last_name,age,dojos_id) Values (%(fname)s,%(lname)s,%(age)s,%(dojos_id)s);")
        new_ninja = mysql.query_db(query,data)
        print(new_ninja)
        return new_ninja