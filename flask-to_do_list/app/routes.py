from flask import render_template, request, redirect, url_for, flash
from app import app
from .forms import SignUpForm, LoginForm, AddForm
import requests, json
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, db
from werkzeug.security import check_password_hash
from urllib.parse import urlencode


@app.route('/login', methods=["POST"])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

   
    user = User.query.filter_by(username=username).first()

    if user:
        if check_password_hash(user.password, password):
            return {
                'status':'Ok',
                'data': user.to_dict()
            }
        else:
            return {
                'status':'Not Ok',
                'message': 'Username or password is incorrect'
            }
    else:
        return{
            'stauts':'Not Ok',
            'message':'User not found'
        }




@app.route('/signup', methods=["POST"])
def signup():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        

        user = User(username,password)

        db.session.add(user)
        db.session.commit()
        return {
            'status':'Ok',
            'message':'Succesfully created new user'
        }
    except:
        return {
            'status':'Not Ok',
            'message':'Could not get user info'
        }
    




