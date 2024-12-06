from flask import Flask
from flask_cors import CORS,cross_origin
from socket import *
import ssl
from routes import configservice

from Configapp import Configapp
from decouple import config
from routes import email

# Routes



app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})


def page_not_found(error):
    return "<h1>Not found page on api</h1>", 404


if __name__ == '__main__':
    app.config.from_object(Configapp['development'])

    app.register_blueprint(email.main, url_prefix='/api/email/')
    app.register_blueprint(configservice.main , url_prefix='/api/config-service/' )
    
    # Error handlers
    app.register_error_handler(404, page_not_found)
    #app.debug = True
    
    #Comentario de ejemplo pull request in python
    
    #app.run(host='192.168.2.62', port=82)
    #porttest=config('PYTHON_PORT')

    app.run(debug=True, host="0.0.0.0", port=85)
    
