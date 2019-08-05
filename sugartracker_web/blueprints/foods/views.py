from flask import Flask, Blueprint, render_template, redirect, request, jsonify, make_response, url_for
import requests
import json
import os
from models.user import User
from models.daily_intake import DailyIntake
import datetime
from flask_login import current_user

foods_blueprint = Blueprint('foods',
                            __name__,
                            template_folder='templates')

@foods_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('foods/new.html')

@foods_blueprint.route('/create', methods=["POST"])
def search():

    nutritionix_id = os.getenv('NUTRITION_APP_ID')
    nutritionix_key = os.getenv('NUTRITION_APP_KEY')

    item_name = request.form['item_name']
    

    response = requests.get(f'https://api.nutritionix.com/v1_1/search/{item_name}?results=0%3A1&fields=nf_total_fat%2Cnf_saturated_fat%2Cnf_trans_fatty_acid%2Cnf_cholesterol%2Cnf_sodium%2Cnf_sugars%2Cnf_calories%2Cnf_calories_from_fat%2Cnf_total_carbohydrate%2Cnf_dietary_fiber%2Cnf_protein%2Cnf_vitamin_a_dv%2Cnf_vitamin_c_dv%2Cnf_calcium_dv%2Cnf_iron_dv&appId={nutritionix_id}&appKey={nutritionix_key}')
    # item_name=item_name, sugar_amount=nf_sugars, calories=nf_calories
    data=(response.json())
    print(data)
    # if not response:
    #     responseObj = {
    #         'status' : 'failed'
    #     }
    #     return render_template('foods/new.html')
    sugar = data['hits'][0]['fields']['nf_sugars']
    calories = data['hits'][0]['fields']['nf_calories']
    DailyIntake.create(item_name=item_name,sugar_amount=sugar,calories=calories,user=current_user.id,date=datetime.datetime.now())
    return make_response(jsonify(data), 200)

@foods_blueprint.route('/<item_name>', methods=["GET"])
def show(item_name):

    nutritionix_id = os.getenv('NUTRITION_APP_ID')
    nutritionix_key = os.getenv('NUTRITION_APP_KEY')

    response = requests.get(f'https://api.nutritionix.com/v1_1/search/{item_name}?results=0%3A1&fields=nf_total_fat%2Cnf_saturated_fat%2Cnf_trans_fatty_acid%2Cnf_cholesterol%2Cnf_sodium%2Cnf_sugars%2Cnf_calories%2Cnf_calories_from_fat%2Cnf_total_carbohydrate%2Cnf_dietary_fiber%2Cnf_protein%2Cnf_vitamin_a_dv%2Cnf_vitamin_c_dv%2Cnf_calcium_dv%2Cnf_iron_dv&appId={nutritionix_id}&appKey={nutritionix_key}')
    data=(response.json())
    
    # print(data)
    # print(data['hits'][0]['fields']['nf_calories'])
    # print(data['hits'][0]['fields']['nf_sugars'])

    # for hits in data['hits'][0]['nf_sugars']:
        # print(hits)

    # response.json.nf_sugars
    # print(json.dumps(item_name))
    # print(json.dumps(response.fields.nf_sugars))

    # item_name = [_['item_name'] for _ in food.json()['data']]

    # for item_name in item_name:
    #     print('item_name')

    return render_template('foods/show.html', item_name=item_name,data=data)
