from flask import Flask, redirect, render_template, request,session
from flask_app import app
from flask_app.models.card import Card


@app.route('/card',methods=['POST'])
def card_create():
    Card.create_card(request.form)
    return redirect('/admin/dashboard#card')



@app.route('/card/edit', methods=['POST'] )
def card_edit():
    if request.form['photo']:
        Card.update_card(request.form)
    else :
        form = {
            'name': request.form['name'],
            'photo':request.form['old_photo'],
        }
        Card.update_card(form)
    return redirect('/admin/dashboard#card')


# Delete
@app.route('/card/delete/<int:id>')
def card_delete(id):
    data={'id':id}
    print('+'*20,data)

    Card.destroy_card(data)
    print('-'*50,Card.destroy_card(data))
    return redirect('/admin/dashboard#card')

# Edit
@app.route('/card/edit/<int:id>')
def card_edit_template(id):
    data={'id':id}
    Card.get_card_by_id(data)
    return render_template('cards_edit.html',car=Card.get_card_by_id(data))



