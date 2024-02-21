from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Raccoon(db.Model):
    
    __tablename__ = "raccoons_table"

    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String, unique=True, nullable=False )
    location = db.Column( db.String )
    has_rabies = db.Column( db.Boolean, default=False )
    img_url = db.Column( db.String )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "has_rabies": self.has_rabies,
            "img_url": self.img_url
        }