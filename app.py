# Created by Samuel Ndubuisi
# On 12th January, 2019
# Credits: https://realpython.com/flask-connexion-rest-api/, https://realpython.com/flask-connexion-rest-api-part-2/

# Python3
# Environment = ussd-app



# Import modules
import os
from flask import render_template as Render
import connexion
from flask_sslify import SSLify # import SSLify for SSL Handling


AppConfig = getattr(__import__('config', fromlist=[os.environ['APP_SETTINGS']]), os.environ['APP_SETTINGS'])

# Application instance
app  = connexion.App(__name__, specification_dir='./')


# Implement SSL Handling
SSLify(app.app)

# Read the Swagger.yml file to configure endpoints
app.add_api('swagger.yml')


# Create URL route for "/"
@app.route('/')
def home():
    """
    """
    return Render('home.html')

if __name__ == '__main__':
    app.run(host=AppConfig.HOST, port=AppConfig.PORT, debug=AppConfig.DEBUG)
