from flask import redirect, Blueprint, render_template, request, flash, url_for,jsonify, make_response
from clarifai.rest import ClarifaiApp
from werkzeug.utils import secure_filename
import os
from app import csrf
from models.daily_intake import DailyIntake
import requests
from flask_login import current_user
import datetime
from highcharts import Highchart


images_blueprint = Blueprint('images',
    __name__, template_folder='templates')


@images_blueprint.route('/new', methods=['GET'])
def new():
    # food_items = DailyIntake.select(item_name, sugar_amount).where()

    # for item in food_items:

    return render_template('images/new.html')

@images_blueprint.route('/check', methods=['POST'])
@csrf.exempt
def check():
    items = request.json #get data from function sendData
    results=[]

    for item in items:

        nutritionix_id = os.getenv('NUTRITION_APP_ID')
        nutritionix_key = os.getenv('NUTRITION_APP_KEY')
        
        response = requests.get(f'https://api.nutritionix.com/v1_1/search/{item}?results=0%3A1&fields=nf_total_fat%2Cnf_saturated_fat%2Cnf_trans_fatty_acid%2Cnf_cholesterol%2Cnf_sodium%2Cnf_sugars%2Cnf_calories%2Cnf_calories_from_fat%2Cnf_total_carbohydrate%2Cnf_dietary_fiber%2Cnf_protein%2Cnf_vitamin_a_dv%2Cnf_vitamin_c_dv%2Cnf_calcium_dv%2Cnf_iron_dv&appId={nutritionix_id}&appKey={nutritionix_key}')
        data=(response.json())
        
        sugar = data['hits'][0]['fields']['nf_sugars']
        calories = data['hits'][0]['fields']['nf_calories']
        u = DailyIntake(item_name=item,sugar_amount=sugar,calories=calories,user=current_user.id,date=datetime.datetime.now())

        if u.save(): #turn into an object, so from object can get the name, data
            nutrition = {
                'item' : item,
                'data': data
            } 
            results.append(nutrition)           
    response = {
        'message':'success',
        'results':results
    }
    return make_response(jsonify(response)), 200
