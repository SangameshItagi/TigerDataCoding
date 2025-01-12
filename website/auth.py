# stores the code for the authorization of the website

from flask import Blueprint, request, jsonify
from .models import User
from . import db
from flask import redirect, url_for
from flask_login import logout_user

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['POST'])
def sign_up():
    email = request.form.get('email')
    password = request.form.get('password')

    new_user = User(email=email, password=password)
    try:
        db.session.add(new_user)
        db.session.commit()
    except:
        db.session.rollback()
        raise
    finally:
        db.session.close()
    user = User.query.filter_by(email=email).first()
    return user.as_dict()

@auth.route('/signout')
def signout():
    logout_user()

    return redirect(url_for('login'))
