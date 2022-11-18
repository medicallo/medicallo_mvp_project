from flask import Flask, redirect, render_template, request
from flask_app import app
from flask_app.models.disease import Disease

# Dashboard
@app.route('/admin/dashboard')
def admin_ds():
    diseases=Disease.get_all_diseases()
    
    return render_template('admin_dashboard.html',diseases=diseases)

# Create
@app.route('/disease', methods=['POST'] )
def disease():
    Disease.create_disease(request.form)
    return redirect('/admin/dashboard')

# Edit
@app.route('/disease/edit/<int:id>')
def disease_edit_template(id):
    data={'id':id}
    Disease.get_disease_by_id(data)
    return render_template('disease_edit.html',hos=Disease.get_disease_by_id(data))

@app.route('/disease/edit', methods=['POST'] )
def disease_edit():

    Disease.update_disease(request.form)
    print('*'*20,Disease.update_disease(request.form))
    return redirect('/admin/dashboard')

# Delete
@app.route('/disease/delete/<int:id>')
def disease_delete(id):
    data={'id':id}

    Disease.destroy_disease(data)
    redirect('/admin/dashboard')