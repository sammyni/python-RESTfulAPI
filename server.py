# Created by Samuel Ndubuisi
# On 12th January, 2019

# Python3
# Environment = ussd-app

from config import Config as AppConfig;

# from flask import (
#     Flask,
#     render_template as Render
# )

from flask import render_template as Render

import connexion

# Import environment class
from config import ProductionConfig as ModeConfig

# Application instance
# app = Flask(__name__, template_folder="templates")
# app.config.from_object(config.DevelopmentConfig)
app  = connexion.App(__name__, specification_dir='./')

# Read the Swagger.yml file to configure endpoints
app.add_api('swagger.yml')




# Create URL route for "/"
@app.route('/')
def home():
    """
    """
    return Render('home.html')

if __name__ == '__main__':
    app.run(debug=ModeConfig.DEBUG)
