from flask import Flask, redirect, render_template, session, request,flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user import User


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/users/new', methods=['POST'])
# def create_user():
#     if User.validate_user(request.form)==False:
#         return redirect('/')
#     pw_hash = bcrypt.generate_password_hash(request.form['password'])
#     print(pw_hash)
#     data={
#         'first_name': request.form['first_name'],
#         'last_name': request.form['last_name'],
#         'email': request.form['email'],
#         'password': pw_hash,

#     }
#     return_from_db=User.create_user(data)
#     print("-"*20, return_from_db,"-"*20)
#     session['user_id']=return_from_db
#     return redirect("/")

    
# @app.route('/login', methods=['POST'])
# def login():
#     # see if the username provided exists in the database
#     data = { "email" : request.form["email"] }
#     user_in_db = User.get_one_by_email(data)
#     # user is not registered in the db
#     if not user_in_db:
#         flash("Invalid Email/Password",'login')
#         return redirect("/")
#     if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
#         # if we get False after checking the password
#         flash("Invalid Email/Password",'login')
#         return redirect('/')
#     # if the passwords matched, we set the user_id into session
#     session['user_id'] = user_in_db.id
#     # never render on a post!!!
#     return redirect("/shows")


# @app.route('/shows')
# def dashboard():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     data={
#         'id':session['user_id']
#     }
#     user=User.get_one_by_id(data)

#     likes=Like.get_like_id(data)
#     return render_template ('dash.html',user=user,shows=Show.get_all(),likes=likes)

# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect('/')