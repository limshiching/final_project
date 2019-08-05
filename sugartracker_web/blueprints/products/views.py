from flask import Blueprint, render_template


products_blueprint = Blueprint('products',
                            __name__,
                            template_folder='templates')
