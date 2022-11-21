from flask import Flask, redirect, render_template, session, request,flash
from flask_app import app
from flask_app.models.admin import Admin

@app.route('/login/admin')
def indef():
    return render_template('log_admin.html')

@app.route('/login_admin',methods=['POST'])
def login_admin():
    admin = Admin.get_admin_by_email(request.form)
    print('**'*20,admin)
    print('*+'*20,admin['password'])
    print('*-'*20,request.form['password'])
    if not admin:
        flash("Invalid Email","login")
        return redirect('/login/admin')
    if not (admin['password'] == request.form['password']):
        flash("Invalid Password","login")
        return redirect('/login/admin')
    session['admin_id'] =admin["id"]
    return redirect('/admin_dashboard')

@app.route('/admin_dashboard')
def dashboard_admin():
    if 'admin_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['admin_id']
    }
    return render_template("admin_dashboard.html")

@app.route('/admin_logout')
def logout_admin():
    session.clear()
    return redirect('/login')