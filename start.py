from app import app
import sugartracker_api
import sugartracker_web
from flask_wtf.csrf import CSRFProtect

if __name__ == '__main__':
    app.run()

csrf=CSRFProtect(app)    
