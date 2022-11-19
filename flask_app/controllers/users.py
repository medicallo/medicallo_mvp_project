from flask import Flask, redirect, render_template, session, request,flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user import User


@app.route('/registration')
def index():
    return render_template('register.html')


@app.route('/login-user')
def indexr():
    return render_template('lo.html')





@app.route('/register',methods=['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.create_user(data)
    session['user_id'] = id
    return redirect('/lo')

@app.route('/login',methods=['POST'])
def login():
    user = User.get_one_by_email(request.form)
    if not user:
        flash("Invalid Email","login")
        return redirect('/lo')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/lo')
    session['user_id'] = user.id
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("dash.html",user=User.get_one_by_id(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')