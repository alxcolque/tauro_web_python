from app import db, bcrypt, app
from flask_login import LoginManager, login_user, logout_user, current_user
from flask import render_template, request, redirect, url_for, flash, session

class WelcomeController():
    def __init__(self):
        pass

    def index(self):
        return render_template('index.html')
    def client(self):
        return render_template('index.html')
    def admin(self):
        return render_template('home.html')

welcomecontroller = WelcomeController()
