from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Product(db.Model):
    product_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # backref so movements can access product
    movements = db.relationship('ProductMovement', back_populates='product')

class Location(db.Model):
    location_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # backref for movements
    from_movements = db.relationship('ProductMovement', foreign_keys='ProductMovement.from_location',
                                     back_populates='from_loc')
    to_movements = db.relationship('ProductMovement', foreign_keys='ProductMovement.to_location',
                                   back_populates='to_loc')

class ProductMovement(db.Model):
    movement_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    from_location = db.Column(db.String, db.ForeignKey('location.location_id'), nullable=True)
    to_location = db.Column(db.String, db.ForeignKey('location.location_id'), nullable=True)
    product_id = db.Column(db.String, db.ForeignKey('product.product_id'), nullable=False)
    qty = db.Column(db.Integer, nullable=False)

    # relationships
    product = db.relationship('Product', back_populates='movements')
    from_loc = db.relationship('Location', foreign_keys=[from_location], back_populates='from_movements')
    to_loc = db.relationship('Location', foreign_keys=[to_location], back_populates='to_movements')
