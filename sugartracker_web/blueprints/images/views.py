from flask import redirect, Blueprint, render_template, request, flash, url_for
from clarifai.rest import ClarifaiApp
from werkzeug.utils import secure_filename
import os
import base64


images_blueprint = Blueprint('images',
    __name__, template_folder='templates')


@images_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('images/new.html')

# @images_blueprint.route('/upload', methods=['POST'])
# def upload():
    # image_file = request.files.get("file") #this will give me the result of file

    # app = ClarifaiApp(api_key=os.getenv('CLARIFAI_KEY'))

    # filename = 
    # model = app.public_models.food_model #give me the food data type
    # response = model.predict_by_filename(filename)
    # results = (response['outputs'][0]['data']['concepts'][3].name) #first 4 list of food
    # doPredict = response.result.split("base64,") [1] #first 2 of food and hash it into base64
    

    # with open("file", "rb") as imageFile:
    #     abc = base64.b64encode(imageFile.read())
    #     print (abc)
    

    # # response.save(os.path.join(app.config.get('upload_photo'), file_name))
    # return json.dumps({'filename': file_name})

    # def reader():
    #     preview  
    #     doPredict({ base64: reader.result.split("base64,")[1] })


    # model = app.public_models.food_model
    # if (response = model.predict_by_url(url='https://samples.clarifai.com/puppy.jpeg'))
    # # app.inputs.create_image_from_url(url='https://samples.clarifai.com/puppy.jpeg')
    # results = (response['outputs'][0]['data']['concepts'][3].name)
    # return render_template('images/new.html', results=results, response=response)