from flask import redirect, Blueprint, render_template, request, flash, url_for,jsonify, make_response
from clarifai.rest import ClarifaiApp
from werkzeug.utils import secure_filename
import os
from app import csrf
from models.daily_intake import DailyIntake


images_blueprint = Blueprint('images',
    __name__, template_folder='templates')


@images_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('images/new.html')

@images_blueprint.route('/check', methods=['POST'])
@csrf.exempt
def check():
    items = request.json #get data from function sendData

    for item in items:
        u = DailyIntake(item_name=item['name'])
        u.save()
        
    response = {
        'message': 'Success'
    }

    return make_response(jsonify(response), 200)




# how to make a chart
# @images_blueprint.route('graph')
# def first_garph():
#     data = {}
#         return render_template('', data=data)

    # for item in request.json:
    #     print(item['name']) #the value is determine value of the image prediction


