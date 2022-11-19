from flask import Flask, redirect, render_template, request,session
from flask_app import app
from flask_app.models.category import Category
from flask_app.models.card import Card
from flask_app.models.hospital import Hospital

@app.route('/home')
def home():
    return render_template('home_landing.html',cards=Card.get_all_card())

@app.route('/diagnostic/<int:id>')
def diagnostic(id):
    session['card_id']=id
    data={'card_id':id}
    categories=Category.get_category_by_card_id(data)

    hospitals=Hospital.get_all_hospital()
    return render_template('description.html',categories=categories,hospitals=hospitals)

@app.route('/region_body',methods=['POST'])
def check():
    session['diseases']=Hospital.get_hospital_with_doc_disease(request.form)
    print('*'*20,session['diseases'])
    card_id=session['card_id']
    return redirect(f'/diagnostic/{card_id}')