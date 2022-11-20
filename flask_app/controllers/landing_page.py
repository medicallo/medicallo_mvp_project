from flask import Flask, redirect, render_template, request,session
from flask_app import app
from flask_app.models.category import Category
from flask_app.models.card import Card
from flask_app.models.hospital import Hospital
from flask_app.models.disease import Disease
from flask_app.models.doctor import Doctor

@app.route('/home')
def home():
    return render_template('home_landing.html',cards=Card.get_all_card())

@app.route('/diagnostic/<int:id>')
def diagnostic(id):
    session['card_id']=id
    data={'card_id':id}
    data_card={'id':id}
    card=Card.get_card_by_id(data_card)
    categories=Category.get_category_by_card_id(data)
    hospitals=Hospital.get_all_hospital()
    return render_template('description.html',categories=categories,hospitals=hospitals,card=card)

@app.route('/region_body',methods=['POST'])
def check():
    session['diseases']=Hospital.get_hospital_with_doc_disease(request.form)
    card_id=session['card_id']
    session['hospital']=Hospital.get_hospital_by_id(request.form)
    return redirect(f'/diagnostic/{card_id}')


@app.route('/disease_diag',methods=['POST'])
def check_disease():
    session['diseases_name']=Disease.get_one_disease(request.form)
    data_doc={'id':session['diseases_name']['doctor_id']}
    print('*-'*20,data_doc)
    session['doctor']=Doctor.get_doctor_by_id(data_doc)
    print('*-'*20,session['doctor'])

    card_id=session['card_id']
    return redirect(f'/diagnostic/{card_id}')

@app.route('/diagnostic/doctor/<int:id>')
def show_doc(id):
    data={
        'id':id
    }
    doctor=Doctor.get_doctor_by_id(data)
    return render_template('doctor_show.html',doctor=doctor) 