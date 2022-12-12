from flask import Flask, redirect, render_template, request,session
from flask_app import app
from flask_app.models.doctor import Doctor
from flask_app.models.hospital import Hospital


@app.route('/doctor_table',methods=['POST'])
def get_doctors():
    data ={
        "id":request.form["hospital_id"]
    }
    session['hospital_name']=Hospital.get_hospital_by_id(data)["name"]
    session['hospital_id']=Doctor.get_doctor_by_hospital_id(request.form)
    return redirect('/admin/dashboard#doctor')


@app.route('/doctor_add',methods=['POST'])
def doctor_create():
    Doctor.create_doctor(request.form)
    return redirect('/admin/dashboard#doctor')



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
    print('*'*50,data)
    doctor_one=Doctor.get_doctor_by_id(data)
    print('*'*50,doctor_one)
    return render_template('doctor_edit.html',zzzz=doctor_one)


@app.route('/doctor/edit', methods=['POST'] )
def doctor_edit():
    if request.form['photo']:
        Doctor.update_doctor(request.form)
    else :
        form = {
            'id':request.form["id"],
            'first_name': request.form['first_name'],
            'last_name':request.form['last_name'],
            'photo':request.form['old_photo'],
            'speciality':request.form['speciality'],
            'about':request.form['about'],
            'hospital_id':request.form['hospital_id']
        }
        Doctor.update_doctor(form)
    
    return redirect('/admin/dashboard')



