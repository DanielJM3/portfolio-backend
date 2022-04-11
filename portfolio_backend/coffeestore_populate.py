from portfolio_backend import app, db, bcrypt
from portfolio_backend.models import User, Items, Shopping_carts
import csv

file = open('portfolio_backend/shopping_data.csv')

csvreader = csv.reader(file)

def generate_list():
    items_list = []

    for row in csvreader:
        items_list.append(row)
    return items_list

def addItem(item_name, popularity, tag, texture, roast_style, taste, cost):
    item = Items(item_name=item_name, popularity=popularity, tag=tag,
                 texture=texture, roast_style=roast_style, taste=taste, cost=cost)
    db.session.add(item)
    db.session.commit()



def populate_database(items_list):
    for item in items_list:
        addItem(item[0], item[1], item[2], item[3], item[4], item[5], item[6])

def create_store():
    populate_database(generate_list())


def addUser(username, password, name):
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(username=username, password=hashed_password, name=name)
    db.session.add(user)
    db.session.commit()

def createShoppingCart(user_id, items):
    cart = Shopping_carts(user_id=user_id, items=items)
    db.session.add(cart)
    db.session.commit()