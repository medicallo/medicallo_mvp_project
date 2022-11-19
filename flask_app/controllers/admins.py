from flask import Flask, redirect, render_template, session, request,flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.admin import Admin

@app.route('/lo/admi')
def indef():
    return render_template('log_admin.html')

@app.route('/login_admin',methods=['POST'])
def login_admin():
    admin = Admin.get_one_by_email(request.form)
    if not admin:
        flash("Invalid Email","login")
        return redirect('/admi')
    if not bcrypt.check_password_hash(admin.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/admi')
    session['admin_id'] =admin.id
    return redirect('/admin_dashboard')

@app.route('/admin_dashboard')
def dashboard_admin():
    if 'admin_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['admin_id']
    }
    return render_template("admin_dashboard.html",admin=Admin.get_by_id(data))

@app.route('/logout')
def logout_admin():
    session.clear()
    return redirect('/admi')