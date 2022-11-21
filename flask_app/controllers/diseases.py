from flask import Flask, redirect, render_template, request,session
from flask_app import app
from flask_app.models.disease import Disease
# from flask_app.models.doctor import Doctor
# from flask_app.models.category import Category


# Create
@app.route('/disease', methods=['POST'] )
def disease():
    Disease.create_disease(request.form)
    return redirect('/admin/dashboard#disease')

# READ
@app.route('/disease_table', methods=['POST'] )
def disease_read():
    # doc_data={'id':request.form['doctor_id"']}
    # first_name=Doctor.get_doctor_by_id(doc_data).first_name
    # session['doctor.f']=first_name
    # last_name=Doctor.get_doctor_by_id(doc_data).last_name
    # session['doctor.l']=last_name

    session['dieseases']=Disease.get_disease_by_ids(request.form)

    return redirect('/admin/dashboard#disease')

# Edit
@app.route('/disease/edit/<int:id>')
def disease_edit_template(id):
    data={'id':id}
    diseases=Disease.get_one_disease(data)
    print('*'*20,diseases)

    return render_template('disease_edit.html',diseases=diseases)

@app.route('/disease/edit', methods=['POST'] )
def disease_edit():

    Disease.update_disease(request.form)
    print('*'*20,Disease.update_disease(request.form))
    return redirect('/admin/dashboard#disease')

# Delete
@app.route('/disease/delete/<int:id>')
def disease_delete(id):
    data={'id':id}
    Disease.destroy_disease(data)
    return redirect('/admin/dashboard#disease')