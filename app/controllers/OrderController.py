from flask import render_template, url_for, request, redirect, flash
from app.models.Order import Order
from app.models.Product import Product
from app.models.User import User
from sqlalchemy import or_
from app import db


class OrderController():
    def __init__(self):
        pass

    def index(self):
        #pedidos = Pedido.query.join(Usuario).filter_by(rol_usuario='cliente').all()
        pedidos = Order.query\
            .join(Product, Product.id==Order.prod_id)\
            .join(User, Order.user_id==User.id)\
            .filter(or_(Order.status == 3, Order.status == 4, Order.status == 5))\
            .all()
        return render_template('orders/index.html', pedidos=pedidos)
    def aceptar(self, _id):
        pedido =  Order.query.get(_id)
        pedido.status = 4
        db.session.commit()
        return redirect(url_for('pedido_router.index'))
    def rechazar(self, _id):
        pedido =  Order.query.get(_id)
        pedido.status = 5
        db.session.commit()
        return redirect(url_for('pedido_router.index'))
    
            
ordercontroller = OrderController()