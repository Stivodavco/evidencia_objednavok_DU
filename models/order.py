from app import db

class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer,primary_key=True)
    customer_id = db.Column(db.Integer,db.ForeignKey("customers.id"))
    product_name = db.Column(db.String)
    quantity = db.Column(db.Integer)
    order_date = db.Column(db.Date)

    def dict(self):
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "product_name": self.product_name,
            "quantity": self.quantity,
            "order_date": self.order_date
        }