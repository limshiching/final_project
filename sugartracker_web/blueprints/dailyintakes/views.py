from flask import Blueprint, render_template


products_blueprint = Blueprint('dailyintakes',
                            __name__,
                            template_folder='templates')
