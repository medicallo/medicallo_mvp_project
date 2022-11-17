from flask import Flask, redirect, render_template, session, request,flash
from flask_app import app
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
from flask_app.models.hospital import Hospital

@app.route('/admin/dashboard')
def admin():
    hospitals=Hospital.get_all_hospital()
    
    return render_template('admin_dashboard.html',hospitals=hospitals)

@app.route('/hospital', methods=['POST'] )
def hospital():
    Hospital.create_hospital(request.form)
    print('*'*20,Hospital.create_hospital(request.form))
    return redirect('/admin/dashboard')

@app.route('/hospital/edit', methods=['POST'] )
def hospital_edit():
    Hospital.update_hospital(request.form)
    print('*'*20,Hospital.create_hospital(request.form))
    return redirect('/admin/dashboard')
