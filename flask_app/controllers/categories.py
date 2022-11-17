from flask import Flask, redirect, render_template, request
from flask_app import app
from flask_app.models.category import Category

# Dashboard
@app.route('/admin/dashboard')
def admin():
    hospitals=Category.get_all_categories()
    
    return render_template('admin_dashboard.html',hospitals=hospitals)

# Create
@app.route('/hospital', methods=['POST'] )
def hospital():
    Category.create_category(request.form)
    return redirect('/admin/dashboard')

# Edit
@app.route('/hospital/edit/<int:id>')
def hospital_edit_template(id):
    data={'id':id}
    Category.get_category_by_id(data)
    return render_template('hospital_edit.html',hos=Category.get_category_by_id(data))

@app.route('/hospital/edit', methods=['POST'] )
def hospital_edit():

    Category.update_category(request.form)
    print('*'*20,Category.update_category(request.form))
    return redirect('/admin/dashboard')

# Delete
@app.route('/hospital/delete/<int:id>')
def hospital_delete(id):
    data={'id':id}
    Category.destroy_category(data)
    return redirect('/admin/dashboard')