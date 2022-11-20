from flask import redirect, render_template, session, request,flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user import User
from flask_app.models.card import Card


@app.route('/')
def index():
    cards=Card.get_all_card()
    return render_template('landing_page.html',cards=cards)


@app.route('/login')
def indexr():
    return render_template('login.html')

@app.route('/register')
def registeration():
    return render_template('signup.html')


@app.route('/signup',methods=['POST'])
def register():
    if User.validate_register(request.form)==False:
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash,
    }
    return_from_db=User.create_user(data)
    print("-"*20, return_from_db,"-"*20)
    session['user_id']=return_from_db
    return redirect('/login')

@app.route('/login',methods=['POST'])
def login():
    user = User.get_one_by_email(request.form)
    if not user:
        flash("Invalid Email","login")
        return redirect('/login')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/login')
    session['user_id'] = user.id
    return redirect('/home')



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')