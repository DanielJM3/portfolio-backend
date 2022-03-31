import os
import codecs
import secrets
import csv
from collections import Counter
import flask
from flask_mail import Message
from flask import Flask, render_template, url_for, flash, redirect, request, abort, send_file, session
from portfolio_backend.forms import LoginForm
from portfolio_backend.models import User, Items, Shopping_carts
from portfolio_backend import app, db, bcrypt, login_manager
from flask_login import login_user, current_user, login_required
import flask_cors
from flask_cors import CORS


####################################
## ROUTES FOR MAIN PORTFOLIO SITE ##
####################################

#################################
## ROUTES FOR SHOPPING WEBSITE ##
#################################

@app.route("/shopping", methods=['GET', 'POST'])
def shopping():
    search = request.get_json()
    shopping_items = Items.query.all()
    payload = []
    for item in shopping_items:
        package = {}
        package['id'] = item.id
        package['item_name'] = item.item_name
        package['popularity'] = item.popularity
        package['tag'] = item.tag
        package['texture'] = item.texture
        package['roast_style'] = item.roast_style
        package['taste'] = item.taste
        package['cost'] = item.cost
        payload.append(package)
    items = flask.jsonify({"items": payload})
    items.headers.add('Access-Control-Allow-Origin', '*')
    return items

@app.route("/add_item_to_cart", methods=['GET', 'POST'])
@flask_cors.cross_origin()
def add_item_to_cart():

    payload = request.get_json()
    item = Items.query.filter_by(id=payload.item)
    shopping_id = payload.id
    shopping_cart = Shopping_carts.filter_by(id=shopping_id)
    if shopping_cart:
        item_not_in_cart = False
        for product in shopping_cart.items:
            if product == item:
                product.amount = product.amount + 1
                item_not_in_cart = True
                break
        if item_not_in_cart == False:
            shopping_cart.items.append({'id': item.id, 'amount': 1})
            db.session.commit()
    else:
        new_cart = Shopping_carts(user_id=shopping_id, items=[{'id': item.id, 'amount': 1}])
        db.session.add(new_cart)
        db.session.commit()




    items = flask.jsonify({"items": 'worked'})
    items.headers.add('Access-Control-Allow-Origin', '*')
    return items

@app.route("/shopping_cart", methods=['GET', 'POST'])
def shopping_cart():
    search = request.get_json()
    cart = Shopping_carts.query.filter_by(id=search)
    for strange in cart:
        list = strange
    print(list.items)
    payload = []
    for item in list.items:
        package = {}
        package['id'] = item['id']
        package['amount'] = item['amount']
        payload.append(package)
    items = flask.jsonify({"items": payload})
    items.headers.add('Access-Control-Allow-Origin', '*')
    return items
