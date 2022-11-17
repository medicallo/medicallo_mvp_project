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
@app.route('/hospital/edit/<int:id>', methods=['POST'] )
def hospital_edit(id):
    Hospital.update_hospital(request.form)
    data={'id':id}
    Hospital.get_hospital_by_id(data)
    return redirect('/admin/dashboard',hos=Hospital.get_hospital_by_id(data))

# Delete
@app.route('/hospital/delete/<int:id>')
def hospital_delete(id):
    data={'id':id}
    print('*'*20,data)

    Hospital.destroy_hospital(data)
    redirect('/admin/dashboard')