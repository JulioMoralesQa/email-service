from flask import Blueprint, jsonify, request, make_response
import json
from email.mime.multipart import MIMEMultipart
import base64
from base64 import b64decode



main = Blueprint('email_blueprint', __name__)
from services.EmailService import EmailService

#* @description: Resetea la contraseña con el codigo de verificacion generado y enviado por email
#? @params: [user_data, subject,html_path,expire_minutes]
#? Retorna de forma estandarizada una respuesta de tipo json al cliente, con un estatus 200
#! En caso de error, manda un estatus 500

main = Blueprint('email_blueprint', __name__)

@main.route('/example-object', methods=['POST'])
def example_object():
    
    
    try:
        
        data= request.json['data']
       
       
        response        = EmailService.send_email("ConfirmacionEmail", "template.html", "ventas@cormago.com.mx", data);
        
        return jsonify(
            message     = ('Error al enviar email','Email enviado correctamente')[response == 200],
            category    = "success",
            data        = response,
            status      = 200,
            registros   = format(1)
        );
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    