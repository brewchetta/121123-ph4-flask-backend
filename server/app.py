#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db # import your models here!

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

# ROUTES #

@app.get('/')
def index():
    return make_response( jsonify("Hello world") )

@app.post('/')
def post_index():
    data = request.json
    data["location"] = "five guys"
    return make_response( jsonify( data ), 201 )

raccoons = [ {}, { "id": 1, "name": "Bob" }, { "id": 2, "name": "Jim" }, { "id": 3, "name": "Frank" } ]

@app.get('/raccoons')
def get_raccoons():
    return make_response( jsonify( raccoons ), 200 )

@app.get('/raccoons/<int:id>')
def get_raccoon_by_id(id):
    raccoon = raccoons[id]
    return make_response( jsonify( raccoon ), 200 )

@app.delete('/raccoons/<int:id>')
def delete_raccoon_by_id(id):
    raccoons.pop(id)
    return {}, 204

if __name__ == '__main__':
    app.run(port=5555, debug=True)