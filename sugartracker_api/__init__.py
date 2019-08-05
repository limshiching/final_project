from app import app,csrf
from flask_cors import CORS

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

## API Routes ##
from sugartracker_api.blueprints.users.views import users_api_blueprint
from sugartracker_api.blueprints.foods.views import foods_api_blueprint

csrf.exempt(users_api_blueprint)
csrf.exempt(foods_api_blueprint)

app.register_blueprint(users_api_blueprint, url_prefix='/api/v1/users')
app.register_blueprint(foods_api_blueprint, url_prefix='/api/v1/foods')
