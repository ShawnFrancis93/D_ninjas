from flask_app import app
from flask_app.models.dojos import dojos
from flask_app.models.ninjas import ninjas
from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template,request, redirect, session

@app.route('/')
def re_index():
    return redirect("/dojos")
    
@app.route('/dojos')
def index():
    
    return render_template("dojos.html", dojos = dojos.get_all())

@app.route('/add_dojo',methods=['POST'])
def add_dojo():
    data ={
        'name':request.form['name'],
    }
    dojos.add(data)
    return redirect("/dojos")

@app.route('/dojos/<id>')
def show_ninjas(id):
    data ={
        'id':id,
    }
    ninja=ninjas.get_all_in_x(data)
    return render_template("show.html",all_ninjas=ninja)

@app.route('/ninjas')
def add_ninjas():
    return render_template("ninjas.html", dojos = dojos.get_all())

@app.route('/add_ninjas',methods=['post'])
def add_new():
    data={
        'dojos_id':request.form['dojos'],
        'fname':request.form['fname'],
        'lname':request.form['lname'],
        'age':request.form['age']
    }
    new_ninjas=ninjas.add_ninjas(data)
    return redirect('/dojos')