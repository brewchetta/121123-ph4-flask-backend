#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Raccoon

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

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
    raccoons = Raccoon.query.all()
    return [ raccoon.to_dict() for raccoon in raccoons ], 200

# GET RACCOON BY ID - SHOW ROUTE
@app.get('/raccoons/<int:id>')
def get_raccoon_by_id(id):
    found_raccoon = Raccoon.query.where(Raccoon.id == id).first()
    if found_raccoon:
        return found_raccoon.to_dict(), 200
    else:
        return { "error": "Not found" }, 404

# POST RACCOON - CREATE ROUTE
@app.post('/raccoons')
def create_raccoon():
    data = request.json

    try:

        new_raccoon = Raccoon(name=data.get("name"), location=data.get("location"), has_rabies=data.get("has_rabies"), img_url=data.get("img_url"))

        db.session.add( new_raccoon )
        db.session.commit()

        return new_raccoon.to_dict(), 201

    except:

        return { "errors": "Invalid raccoon please try again" }, 406


# PATCH RACCOON BY ID - UPDATE ROUTE
@app.patch('/raccoons/<int:id>')
def update_raccoon(id):
    data = request.json
    found_raccoon = Raccoon.query.where(Raccoon.id == id).first()

    if found_raccoon:

        try:
            for key in data:
                setattr( found_raccoon, key, data[key] )
            db.session.commit()
            return found_raccoon.to_dict(), 202

        except:
            return { "error": "Invalid raccoon" }, 406
    
    else:
        return { "error": "Not found" }, 404


# DELETE RACCOON BY ID - DELETE ROUTE
@app.delete('/raccoons/<int:id>')
def delete_raccoon(id):
    found_raccoon = Raccoon.query.where(Raccoon.id == id).first()

    if found_raccoon:

        db.session.delete(found_raccoon)
        db.session.commit()

        return {}, 204
    
    else:
        return { "error": "Not found" }, 404
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)