from flask import Blueprint, render_template
from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from models.user import User
from flask_login import login_required, current_user
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


@users_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass


@users_blueprint.route('/', methods=["GET"])
def index():
    return "USERS"


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass
