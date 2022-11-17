from flask import Flask, redirect, render_template, session, request,flash
from flask_app import app
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
from flask_app.models.hospital import Hospital

# Dashboard
@app.route('/admin/dashboard')
def admin():
    hospitals=Hospital.get_all_hospital()
    
    return render_template('admin_dashboard.html',hospitals=hospitals)

# Create
@app.route('/hospital', methods=['POST'] )
def hospital():
    Hospital.create_hospital(request.form)
    return redirect('/admin/dashboard')

# Edit
@app.route('/hospital/edit/<int:id>')
def hospital_edit_template(id):
    data={'id':id}
    Hospital.get_hospital_by_id(data)
    return render_template('hospital_edit.html',hos=Hospital.get_hospital_by_id(data))

@app.route('/hospital/edit', methods=['POST'] )
def hospital_edit():

    Hospital.update_hospital(request.form)
    print('*'*20,Hospital.update_hospital(request.form))
    return redirect('/admin/dashboard')

# Delete
@app.route('/hospital/delete/<int:id>')
def hospital_delete(id):
    data={'id':id}

    Hospital.destroy_hospital(data)
    redirect('/admin/dashboard')