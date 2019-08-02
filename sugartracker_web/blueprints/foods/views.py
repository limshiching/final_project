from flask import Flask, Blueprint, render_template, redirect, request, jsonify, make_response, url_for
import requests
import json
import os
from models.user import User

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

    item_name = request.form.get('item_name')

    response = requests.get(f'https://api.nutritionix.com/v1_1/search/{item_name}?fields=nf_sugars%2Cnf_calories%2Cnf_calories_from_fat%2Cnf_total_carbohydrate&appId={nutritionix_id}&appKey={nutritionix_key}')
    data=(response.json())

    if not response:
        responseObj = {
            'status' : 'failed'
        }
        return render_template('foods/new.html')

    # return make_response(jsonify(data), 200)
    return redirect(url_for('foods.show', item_name=item_name))

@foods_blueprint.route('/<item_name>', methods=["GET"])
def show(item_name):

    nutritionix_id = os.getenv('NUTRITION_APP_ID')
    nutritionix_key = os.getenv('NUTRITION_APP_KEY')

    response = requests.get(f'https://api.nutritionix.com/v1_1/search/{item_name}?fields=nf_sugars%2Cnf_calories%2Cnf_calories_from_fat%2Cnf_total_carbohydrate&appId={nutritionix_id}&appKey={nutritionix_key}')
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
