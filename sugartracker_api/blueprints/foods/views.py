from flask import Blueprint, jsonify, make_response
import requests


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
            'sugar' : food.sugars
        })
    response = {'data': food_list}
    return make_response(jsonify(response), 200)

@foods_api_blueprint('/<item_name>/', methods=['GET'])
def search():





