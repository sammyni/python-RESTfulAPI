# Created by Samuel Ndubuisi
# On 12th January, 2019
# Credits: https://realpython.com/flask-connexion-rest-api/, https://realpython.com/flask-connexion-rest-api-part-2/

# Python3
# Environment = ussd-app

# Import modules
import os
import connexion
from flask_sslify import SSLify # import SSLify for SSL Handling
from flask import render_template as Render
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Get configuration data to run app
AppConfig = getattr(__import__('config', fromlist=[os.environ['APP_SETTINGS']]), os.environ['APP_SETTINGS'])

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# Configure underlying flask app instance
app.config.from_object(f"config.{os.environ['APP_SETTINGS']}")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Implement SSL Handling
SSLify(app)

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

# Import models for migration
from models import Person

# Read the Swagger.yml file to configure endpoints
connex_app.add_api('swagger.yml')

# Create URL route for "/"
@app.route('/')
def home():
    """
    """
    return Render('home.html')

if __name__ == '__main__':
    connex_app.run(host=AppConfig.HOST, port=AppConfig.PORT, debug=AppConfig.DEBUG)
