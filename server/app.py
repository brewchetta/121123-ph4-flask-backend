#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Raccoon

app = Flask(__name__)
# TODO: For tomorrow import and add in cors here!
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

# ROUTES #

@app.get('/')
def index():
    return make_response( jsonify( "--Welcome to my raccoon flask app--" ) )

# RACCOONS ROUTES #

# GET ALL RACCOONS - INDEX ROUTE
@app.get('/raccoons')
def get_raccoons():
    pass

# GET RACCOON BY ID - SHOW ROUTE
@app.get('/raccoons/<int:id>')
def get_raccoon_by_id(id):
    pass

# POST RACCOON - CREATE ROUTE

# PATCH RACCOON BY ID - UPDATE ROUTE

# DELETE RACCOON BY ID - DELETE ROUTE

if __name__ == '__main__':
    app.run(port=5555, debug=True)