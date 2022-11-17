from flask import Flask, redirect, render_template, session, request,flash
from flask_app import app
from flask_app.models.doctor import Doctor

@app.route('/admin/dashboard')
def doc():
    doctors=Doctor.get_all()
    
    return render_template('admin_dashboard.html',doctors=doctors)


@app.route('/doctor',methods=['POST'])
def doctor():
    Doctor.create_doctor(request.form)
    print('*'*20,Doctor.create_doctor(request.form))
    return redirect('/admin/dashboard')


@app.route('/doctor/edit', methods=['POST'] )
def doctor_edit():
    Doctor.update(request.form)
    print('*'*20,Doctor.update(request.form))
    return redirect('/admin/dashboard')


# Delete
@app.route('/doctor/delete/<int:id>')
def hospital_delete(id):
    data={'id':id}

    Doctor.destroy(data)
    return redirect('/admin/dashboard')

# Edit
@app.route('/hospital/edit/<int:id>')
def doctor_edit_template(id):
    data={'id':id}
    Doctor.get_doctor_by_id(data)
    return render_template('doctor_edit.html',doc=Doctor.get_doctor_by_id(data))



