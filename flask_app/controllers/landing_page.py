from flask import Flask, redirect, render_template, request
from flask_app import app
from flask_app.models.card import Card

@app.route('/home')
def home():
    return render_template('home_landing.html',cards=Card.get_all_card())

@app.route('/diagnostic')
def diagnostic():
    return render_template('description.html')