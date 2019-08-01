from flask import Flask, Blueprint, render_template, request, redirect
from models.user import User

@app.before_request
def before_request():
    db.connect()


@app.after_request
def after_request(response):
    db.close()
    return response


@app.cli.command()
def migrate():
    db.evolve(ignore_tables={'base_model'})

foods_blueprint = Blueprint('foods',
                            __name__,
                            template_folder='templates')

@foods_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('foods/new.html')


@foods_blueprint.route('/<item_name>', methods=["GET"])
def search(item_name):
    food = 