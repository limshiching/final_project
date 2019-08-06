from flask import redirect, Blueprint, render_template, request, flash, url_for,jsonify
from clarifai.rest import ClarifaiApp
from werkzeug.utils import secure_filename
import os
from app import csrf


images_blueprint = Blueprint('images',
    __name__, template_folder='templates')


@images_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('images/new.html')

@images_blueprint.route('/upload', methods=['POST'])
@csrf.exempt
breakpoint()
    # data = request.form.get('concepts')
    # print(data)

    # return jsonify({
    #     'ok': True
    # })
    # if not data:
    #     return jsonify({
    #         'message': 'Failed' 
    # })
    # for nutritionData in stat:
    #     get_food_on_status = DailyIntake.get_or_none(food_stage=nutritionData)
    #     for food in get_food_on_status:
    #         food_on_status_list.append(food)
    
    # s = DailyIntake(stat=stat)

    # if s.save():
    #     flash('Succefully saved')
    #     return redirect(url_for('images.new'))


