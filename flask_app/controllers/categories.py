from flask import Flask, redirect, render_template, request,session
from flask_app import app
from flask_app.models.category import Category
from flask_app.models.card import Card


# Create
@app.route('/category/popup', methods=['POST'] )
def category_create():
    Category.create_category(request.form)
    return redirect('/admin/dashboard#category')

@app.route('/category', methods=['POST'] )
def category_get_by_card():
    data={"id":request.form['card_id']}
    card=Card.get_card_by_id(data)
    session['card_name']=card["name"]
    print("-"*50,session['card_name'])
    session['categories']=Category.get_category_by_card_id(request.form)
    return redirect('/admin/dashboard#category')

# Edit
@app.route('/category/edit/<int:id>')
def category_edit_template(id):
    data={'id':id}
    category=Category.get_category_by_id(data)
    return render_template('category_edit.html',category=category)

@app.route('/category/edit', methods=['POST'] )
def categorie_edit():

    Category.update_category(request.form)
    print('*'*20,Category.update_category(request.form))
    return redirect('/admin/dashboard#category')

# Delete
@app.route('/category/delete/<int:id>')
def categorie_delete(id):
    data={'id':id}
    Category.destroy_category(data)
    return redirect('/admin/dashboard#category')