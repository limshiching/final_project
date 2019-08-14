from app import app
from flask import render_template, Blueprint, url_for
from flask_assets import Environment, Bundle
from .util.assets import bundles
import os
import config
from sugartracker_web.util.oauth import oauth
import chartkick 

assets = Environment(app)
assets.register(bundles)
oauth.init_app(app)

from sugartracker_web.blueprints.users.views import users_blueprint
from sugartracker_web.blueprints.images.views import images_blueprint
from sugartracker_web.blueprints.foods.views import foods_blueprint
from sugartracker_web.blueprints.sessions.views import sessions_blueprint

app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(images_blueprint, url_prefix="/images")
app.register_blueprint(foods_blueprint, url_prefix="/foods")
app.register_blueprint(sessions_blueprint, url_prefix="/sessions")
app.jinja_env.add_extension("chartkick.ext.charts")

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

