from flask import redirect, Blueprint, render_template, request, flash, url_for
from clarifai.rest import ClarifaiApp
from werkzeug.utils import secure_filename
import os


images_blueprint = Blueprint('images',
    __name__, template_folder='templates')


@images_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('images/new.html')

@images_blueprint.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('user_file')
    breakpoint()
    # url_input = request.params['url_input']
    
    app = ClarifaiApp(api_key=os.getenv('CLARIFAI_KEY'))

    # if not file.filename:
        # return 'Please select a file'
    # print(file.filename)
    model = app.public_models.food_model
    response = model.predict_by_url(url='https://samples.clarifai.com/puppy.jpeg')
    # app.inputs.create_image_from_url(url='https://samples.clarifai.com/puppy.jpeg')
    results = (response['outputs'][0]['data']['concepts'])
    return render_template('images/new.html', results=results, response=response)