from flask import Flask, Blueprint, render_template, redirect, request, jsonify, make_response
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

    response = requests.get(f'https://api.nutritionix.com/v1_1/search/{item_name}?fields=nf_sugars%2Cnf_calories%2Cnf_calories_from_fat%2Cnf_total_carbohydrates&appId={nutritionix_id}&appKey={nutritionix_key}')
    data=(response.json())

    if not response:
        responseObj = {
            'status' : 'failed'
        }
        return render_template('foods/new.html')

    return make_response(jsonify(data), 200)