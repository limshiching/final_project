from flask import redirect, Blueprint, render_template
from clarifai.rest import ClarifaiApp

images_blueprint = Blueprint('images',
    __name__, template_folder='templates')


@images_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('images/new.html')

@images_blueprint.route('/upload', methods=['POST'])
def upload():

    file = request.files['user_file']
    if 'file' not in request.files:
        return "No file"

    image = request.form.get('image_name')

    app = ClarifaiApp(api_key='5b3b1ba9fc7546b591655e33f31052af')
    model = app.public_models.general_model
    response = model.predict_by_url(image)

    if response.save():
        flash('Upload Successful')
        return redirect(url_for('image.new'))
    
    else:
        return redirect(url_for('images.new'))