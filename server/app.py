#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    
    bake_goods = []
    for goods in Bakery.query.all():
        bake_dict = goods.to_dict()
        bake_goods.append(bake_dict)

    response = make_response(
        bake_goods,
        200,
        {"Content-Type": "application/json"}
    )

    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    
    bakery = Bakery.query.filter(Bakery.id == id).first()

    bake_dict = bakery.to_dict()

    response = make_response(
        bake_dict,
        200
    )

    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    
    bake_goods = []
    for goods in BakedGood.query.order_by(BakedGood.price.desc()):
        bake_dict = goods.to_dict()
        bake_goods.append(bake_dict)

    response = make_response(
        bake_goods,
        200,
        {"Content-Type": "application/json"}
    )

    return response

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    
    expensive = BakedGood.query.order_by(BakedGood.price.desc()).first()

    bake_dict = expensive.to_dict()

    response = make_response(
        bake_dict,
        200
    )

    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
