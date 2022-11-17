from flask import Flask, redirect, render_template, request,session
from flask_app import app
from flask_app.models.doctor import Doctor

@app.route('/doctor_table',methods=['POST'])
def get_doctors():
    session['hospital_id']=Doctor.get_doctor_by_hospital_id(request.form)
    return redirect('/admin/dashboard')

@app.route('/admin/dashboard')
def get_doc(): 
    print('*'*20,session['hospital_id'])

    return render_template('admin_dashboard.html', all_doctors=session['hospital_id'])

@app.route('/doctor',methods=['POST'])
def doctor():
    
    return redirect('/admin/dashboard')


@app.route('/doctor/edit', methods=['POST'] )
def doctor_edit():
    Doctor.update_doctor(request.form)
    print('*'*20,Doctor.update_doctor(request.form))
    return redirect('/admin/dashboard')


# Delete
@app.route('/doctor/delete/<int:id>')
def doctor_delete(id):
    data={'id':id}
    Doctor.destroy_doctor(data)
    return redirect('/admin/dashboard')

# Edit
@app.route('/doctor/edit/<int:id>')
def doctor_edit_template(id):
    data={'id':id}
    return render_template('doctor_edit.html',doc=Doctor.get_doctor_by_id(data))



