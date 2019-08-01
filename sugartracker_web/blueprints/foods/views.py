from flask import Flask, Blueprint, render_template, request, redirect
from models.user import User

foods_blueprint = Blueprint('foods',
                            __name__,
                            template_folder='templates')

@foods_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('foods/new.html')


@foods_blueprint.route('/<item_name>', methods=["GET"])
def search(item_name):
    pass