from flask import Blueprint, render_template
from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from models.user import User
from flask_login import login_required, current_user
from sugartracker_web.util.oauth import oauth
import app
import os



users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')


@users_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('users/new.html')


@users_blueprint.route('/create', methods=['POST'])
def create():
    name = request.form.get("fullname")
    email = request.form.get('email')
    password = request.form.get('pwd')
    gender = request.form.get('gender')
    length = request.form.get('length')
    DOB = request.form.get('date')
   
    hashed_password = generate_password_hash(password)
    user = User(name=name, email=email,
                password=hashed_password, gender=gender, length=length, DOB=DOB)
    if user.save():
        return redirect(url_for('home'))
    else:
        return redirect(url_for('users.new'))


@users_blueprint.route('/google', methods=["GET"])
def google():
    redirect_uri = "http://localhost:5000/users/google/login"
    return oauth.google.authorize_redirect(redirect_uri)


@users_blueprint.route('/google/login', methods=["GET"])
def google_login():
    token = oauth.google.authorize_access_token()
    profile = oauth.google.get(
        'https://www.googleapis.com/oauth2/v2/userinfo').json()
    name =profile['name']
    email = oauth.google.get(
        'https://www.googleapis.com/oauth2/v2/userinfo').json()['email']
    return redirect(url_for('home'))
     


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass
