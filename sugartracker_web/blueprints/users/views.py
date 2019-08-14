from flask import Blueprint, render_template
from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from models.user import User
from models.daily_intake import DailyIntake
import datetime
from flask_login import login_required, current_user, login_user, login_manager
from sugartracker_web.util.oauth import oauth
import app
import os
import math


users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')


@users_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('users/new.html')


@users_blueprint.route('/create', methods=['POST', 'GET'])
def create():
    name = request.form.get("fullname")
    email = request.form.get('email')
    password = request.form.get('password')
    gender = request.form.get('gender')
    length = request.form.get('length')
    weight = request.form.get('weight')
    activity = request.form.get('activity')
    DOB = request.form.get('date')
    pwd = generate_password_hash(password)

    user = User(name=name, email=email,
                password=pwd, gender=gender, length=length, DOB=DOB, weight=weight, activity=activity)
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
    name = profile['name']
    email = oauth.google.get(
        'https://www.googleapis.com/oauth2/v2/userinfo').json()['email']
    user = User.get_or_none(User.email == email)
    if user == None:
        user = User(name=name, email=email)
        if user.save():
            login_user(user)
            return redirect(url_for('users.edit'))
        else:
            return redirect(url_for('users.create'))
    else:
        login_user(user)
        flash('Welcome, successfully signed in.')
        return redirect(url_for('home', id=user.id))


@users_blueprint.route('/facebook', methods=["GET"])
def facebook():
    redirect_uri = "http://localhost:5000/users/facebook/login"
    return oauth.facebook.authorize_redirect(redirect_uri, state=session['csrf_token'])


@users_blueprint.route('/facebook/login', methods=["GET"])
def facebook_login():
    token = oauth.facebook.authorize_access_token()
    facebook_id = oauth.facebook.get(
        "https://graph.facebook.com/v3.2/me").json()["id"]

    user_data = oauth.facebook.get(
        f"https://graph.facebook.com/v3.2/{facebook_id}?fields=id,name,email").json()
    email = user_data['email']
    name = user_data['name']

    user = User.get_or_none(User.email == email)
    if user == None:
        user = User(name=name, email=email)
        if user.save():
            login_user(user)
            return redirect(url_for('users.edit'))
        else:
            return redirect(url_for('users.create'))
    else:
        login_user(user)
        flash('Welcome, successfully signed in.')
        return redirect(url_for('home', id=user.id))


@users_blueprint.route('/edit', methods=["GET"])
def edit():
    return render_template('users/edit.html')


@users_blueprint.route('/update', methods=['POST', 'GET'])
def update():
    user_id = current_user.id
    user = User.get_by_id(user_id)
    user.DOB = request.form.get('date')
    user.gender = request.form.get('gender')
    user.activity = request.form.get('activity')
    user.length = request.form.get('length')
    user.weight = request.form.get('weight')
    password = request.form.get('pwd')
    user.password = generate_password_hash(password)
    if user.save():
        return redirect(url_for('home'))
    else:
        return redirect(url_for('users.create'))


@users_blueprint.route('/show', methods=['GET', 'POST'])
@login_required
def show():
    user = User.get_by_id(current_user.id)
    year = ""
    user_list = ""
    age = 0
    BMR = 0
    Calories = 0
    userbirth = user.DOB
    user_split = user.DOB.split("-")
    user_list = user_split[0]
    birthyear = "".join(user_list)
    birthm = user_split[1]
    birthmonth = int("".join(birthm))
    birthyear_int = int(birthyear)
    today = datetime.date.today()
    year = today.strftime("%Y")
    month = int(today.strftime("%m"))
    year_int = int(year)
    if month > birthmonth:
        age = year_int - birthyear_int
    else:
        age = (year_int - birthyear_int)-1
    if user.gender == 'Female':
        BMR = (10*int(user.weight))+(6.25*int(user.length))-(5*age)-161
    else:
        BMR = (10*int(user.weight))+(6.25*int(user.length))-(5*age)+5

    if user.activity == 'Very light':
        Calories = BMR*1.2
    elif user.activity == 'Light':
        Calories = BMR*1.375
    elif user.activity == 'Moderate':
        Calories = BMR*1.55
    elif user.activity == 'Heavy':
        Calories = BMR*1.725
    else:
        Calories = BMR*1.9

    calories = round(Calories)
    cal = Calories-2000
    cal2000 = cal/2000
    cal90 = 90*cal2000
    sugar_daily = round(90+(cal90))

    weight = user.weight
    activity = user.activity
    food_sugar = DailyIntake.select().dicts()
    sugar_amount = 0 
    calorie_amount = 0
    for food in food_sugar:
        if food['user'] == current_user.id:
            if food['date'] == datetime.date.today():
                if food['sugar_amount']== None or food['sugar_amount']== 'Null':
                    sugar_amount = 0
                else:    
                    sugar_amount += round(food['sugar_amount'])
                    calorie_amount += round(food['calories'])

    if sugar_amount == 0:
        percentage_sugar = 0
        sugar_left = sugar_daily
    else:
        percentage_sugar = round(sugar_daily/sugar_amount*100)
        sugar_left = sugar_daily - sugar_amount
    if calorie_amount == 0:
        percentage_calories = 0
        calories_left = calories
    else:
        percentage_calories = round(calories/calorie_amount*100)
        calories_left = calories-calorie_amount
        if calories_left < 0:
            calories_left = 0

    return render_template('users/show.html', ps=percentage_sugar, sl=sugar_left, pc=percentage_calories, cl=calories_left, weight=weight, activity=activity, sugar_daily=sugar_daily, sugar_amount=sugar_amount, cal_intake=calories, calorie_amount=calorie_amount)


@users_blueprint.route('/info', methods=['POST', 'GET'])
@login_required
def info():
    return render_template('users/info.html')


@users_blueprint.route('/change', methods=['POST', 'GET'])
@login_required
def change():
    user = User.get_by_id(current_user.id)
    user.weight = request.form.get('weight')
    user.activity = request.form.get('activity')
    if user.save():
        return redirect(url_for('users.show'))
