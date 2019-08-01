from flask import Blueprint, jsonify, make_response
import requests
import os
import json

foods_api_blueprint = Blueprint('foods_api',
                             __name__,
                             template_folder='templates')


@foods_api_blueprint.route('/', methods=['GET'])
def index():
    food = Food.select()
    food_list = []
    for food in foods:
        food_list.append({
            'id' : food.item_id,
            'brand' : food.brand_name,
            'calories' : food.calories,
            'unit' : food.calories_unit,
            'sugar' : food.nf_sugars
        })

    response = {'requests.get(https://api.nutritionix.com/v1_1/)' : food_list} 
  
    return make_response(jsonify(response), 200)

@foods_api_blueprint.route('/<item_name>', methods=['GET'])
def search(item_name):
    # foods = Food.select()
    # food_list = []
    # for food in foods:
    #     food_list.append({
    #         'id' : food.item_id,
    #         'brand' : food.brand_name,
    #         'calories' : food.calories,
    #         'unit' : food.calories_unit,
    #         'sugar' : food.sugars
    #     })

    nutritionix_id = os.getenv('NUTRITION_APP_ID')
    nutritionix_key = os.getenv('NUTRITION_APP_KEY')

    response = requests.get(f'https://api.nutritionix.com/v1_1/search/{item_name}?appId={nutritionix_id}&appKey={nutritionix_key}')
    data=(response.json())
    
    if not response:
        responseObj = {
            'status':'failed'
        }
        return make_response(jsonify(responseObj), 400)
    return make_response(jsonify(data),200)







