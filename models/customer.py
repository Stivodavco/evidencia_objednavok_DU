from sqlalchemy.orm import backref

from app import db

class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(100))
    orders = db.relationship("Order", backref="customer")

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }