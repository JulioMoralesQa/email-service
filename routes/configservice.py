from flask import Blueprint, jsonify, request, make_response
import json
from email.mime.multipart import MIMEMultipart
import base64
from base64 import b64decode
import io
import os
# Models

from models.StandardModel import StandardModel


main = Blueprint('configservice_blueprint', __name__)
IMAGE_PATH = "/appbizion/";

@main.route('/add-new-service', methods=['POST'])
def add_new_service():
    
    
    try:
        config = request.json['new-service']

        with open('/appbizion/config.json','r') as rb:

            data = json.load(rb)
            print(data)
            newdata= json.dumps(config)
            data.update(config)
            print(data)

        with open('/appbizion/config.json','w') as wb:
            
            json.dump(data, wb, indent=4)

        response = data                  
        
        
        return jsonify(
            message     = ('Servicio agregado')[response == 200],
            category    = "success",
            data        = response,
            status      = 200,
            registros   = format(1)
        );
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500