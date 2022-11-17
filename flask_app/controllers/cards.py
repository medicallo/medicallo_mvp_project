from flask import Flask, redirect, render_template, session, request,flash
from flask_app import app
from flask_app.models.card import Card

@app.route('/admin/dashboard')
def car():
    cards=Card.get_all()
    
    return render_template('admin_dashboard.html',cards=cards)


@app.route('/card',methods=['POST'])
def card_create():
    Card.create_card(request.form)
    print('*'*20,Card.create_card(request.form))
    return redirect('/admin/dashboard')


@app.route('/card/edit', methods=['POST'] )
def card_edit():
    Card.update(request.form)
    print('*'*20,Card.update(request.form))
    return redirect('/admin/dashboard')


# Delete
@app.route('/card/delete/<int:id>')
def card_delete(id):
    data={'id':id}

    Card.destroy(data)
    return redirect('/admin/dashboard')

# Edit
@app.route('/card/edit/<int:id>')
def card_edit_template(id):
    data={'id':id}
    Card.get_card_by_id(data)
    return render_template('card_edit.html',car=Card.get_card_by_id(data))



