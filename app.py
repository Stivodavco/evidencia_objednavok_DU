from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://uebgnhah6kbsv38depmb:5V2d7U6YdLMoiITYuD52SuX7xMWo16@bjjn1h84m9frvsxxgy7u-postgresql.services.clever-cloud.com:50013/bjjn1h84m9frvsxxgy7u'
db = SQLAlchemy(app)

from models.customer import Customer
from models.order import Order

@app.route('/customers')
def get_all_customers():
    customer_objects = Customer.query.all()
    customers = []

    for customer in customer_objects:
        customers.append(customer.dict())

    return jsonify(customers), 200

@app.route('/orders')
def get_all_orders():
    order_objects = Order.query.all()
    orders = []

    for order in order_objects:
        orders.append(order.dict())

    return jsonify(orders), 200

@app.route('/customers/<customer_id>/orders', methods=["GET"])
def get_orders_for_customer(customer_id):
    customer = Customer.query.get(customer_id)

    if not customer:
        return "Customer not found", 404

    order_objects = customer.orders
    orders = []
    for order in order_objects:
        orders.append(order.dict())

    return jsonify(orders), 200

@app.route('/customers/<customer_id>/orders', methods=["POST"])
def create_order_for_customer(customer_id):
    data = request.json

    customer = Customer.query.get(customer_id)

    if not customer:
        return "Customer not found", 404

    new_order = Order()
    new_order.customer_id = customer.id
    new_order.product_name = data["product_name"]
    new_order.quantity = data["quantity"]
    new_order.order_date = datetime.today()

    db.session.add(new_order)
    db.session.commit()

    return jsonify(new_order.dict()), 200

@app.route('/orders/<order_id>', methods=["PUT"])
def edit_order(order_id):
    data = request.json

    order = Order.query.get(order_id)

    if not order:
        return "Order not found", 404

    order.product_name = data["product_name"]
    order.quantity = data["quantity"]
    order.order_date = data["order_date"]

    db.session.commit()

    return jsonify(order.dict()), 200

@app.route('/orders/<order_id>', methods=["DELETE"])
def delete_order(order_id):
    data = request.json

    order = Order.query.get(order_id)

    if not order:
        return "Order not found", 404

    db.session.delete(order)
    db.session.commit()

    return "Order successfully deleted", 200


if __name__ == '__main__':
    app.run()
