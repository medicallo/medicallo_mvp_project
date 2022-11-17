from flask import Flask, redirect, render_template, request
from flask_app import app
from flask_app.models.category import Category

# Dashboard
@app.route('/admin/dashboard')
def admin_hp():
    categories=Category.get_all_categories()
    
    return render_template('admin_dashboard.html',categories=categories)

# Create
@app.route('/category', methods=['POST'] )
def category():
    Category.create_category(request.form)
    return redirect('/admin/dashboard')

# Edit
@app.route('/category/edit/<int:id>')
def category_edit_template(id):
    data={'id':id}
    Category.get_category_by_id(data)
    return render_template('categorie_edit.html',hos=Category.get_category_by_id(data))

@app.route('/category/edit', methods=['POST'] )
def categorie_edit():

    Category.update_category(request.form)
    print('*'*20,Category.update_category(request.form))
    return redirect('/admin/dashboard')

# Delete
@app.route('/categorie/delete/<int:id>')
def categorie_delete(id):
    data={'id':id}
    Category.destroy_category(data)
    return redirect('/admin/dashboard')