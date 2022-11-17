from flask import Flask, redirect, render_template, request
from flask_app import app
from flask_app.models.doctor import Doctor

@app.route('/admin/dashboard')
def doc():
    doctors=Doctor.get_all()
    
    return render_template('admin_dashboard.html',doctors=doctors)


@app.route('doctor',methods=['POST'])
def doctor():
    Doctor.create_doctor(request.form)
    print('*'*20,Doctor.create_doctor(request.form))
    return redirect('/admin/dashboard')


@app.route('/doctor/edit', methods=['POST'] )
def doctor_edit():
    Doctor.update(request.form)
    print('*'*20,Doctor.update(request.form))
    return redirect('/admin/dashboard')


@app.route('/doctor/delete', methods=['POST'] )
def doctor_edit():
    Doctor.destroy(request.form)
    print('*'*20,Doctor.destroy(request.form))
    return redirect('/admin/dashboard')


