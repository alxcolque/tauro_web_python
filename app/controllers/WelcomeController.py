from app.models.Client import Client
from app import db, bcrypt, app
from flask_login import LoginManager, login_user, logout_user, current_user
from flask import render_template, request, redirect, url_for, flash, session
from app.models.Product import Product
from app.models.Category import Category
from app.models.User import User
from app.models.Order import Order
from app.models.OrderDetail import OrderDetail

class WelcomeController():
    def __init__(self):
        pass

    def index(self):

        producto = Product.query.all()
        category = Category.query.all()
        
        return render_template('index.html', producto = producto, categories=category)
    def client(self):
        producto = Product.query.all()
        category = Category.query.all()
        #user_id = current_user.id
        cart = OrderDetail.query\
            .join(Product, Product.id==OrderDetail.product_id)\
            .all()

        total = db.session.query(db.func.sum(Order.total))\
            .filter(Order.status == 1)\
            .scalar()
        return render_template('index.html', producto = producto, categories=category,cart=cart, total=total)
    def admin(self):
        cusuario = User.query.count()
        cpedido = Order.query.count()
        cproducto = Product.query.count()
        ccategoria = Category.query.count()
        cclientes = Client.query.count()
        users = User.query.all()
        return render_template('home.html', users=users, cusuario=cusuario, cpedido=cpedido, cproducto=cproducto,ccategoria=ccategoria,cclientes=cclientes)

welcomecontroller = WelcomeController()
