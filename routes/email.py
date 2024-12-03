from flask import Blueprint, jsonify, request, make_response
import json
from email.mime.multipart import MIMEMultipart
import base64
from base64 import b64decode
# Models

from models.StandardModel import StandardModel


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
    
@main.route('/save-email-la-perla', methods=['POST'])
def saveMailLaPerla():
    
    
    try:
        
        data= request.json['data']
        sig = [{"email":data}]
        datasig= json.dumps(sig)
        params=(1,datasig)
        storeProcedure="\"LaPerlaWeb\".\"EmailOperations\""
        note_data   = StandardModel.standar_query(storeProcedure,params)
        print("linea 53")
        print(note_data)
        email           = MIMEMultipart();
        email['info']   = 'Gracias por suscribirte a la perla';
        email['option'] = 'html';
        response        = EmailService.send_email_la_perla("ConfirmacionEmail", "templateRevistaLaPerla.html", data, email);
        
        return jsonify(
            message     = ('Error al enviar email','Email enviado correctamente')[response == 200],
            category    = "success",
            data        = response,
            status      = 200,
            registros   = format(1)
        );
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/send-email-gafimex', methods=['POST'])
def sendEmailGafimex():
    
    
    try:
        
        data= request.json['data']
       
        response        = EmailService.send_email("ConfirmacionEmail", "templateGafimex.html", "jmorales-webdev@hyvecode.com.mx", data);
        
        return jsonify(
            message     = ('Error al enviar email','Email enviado correctamente')[response == 200],
            category    = "success",
            data        = response,
            status      = 200,
            registros   = format(1)
        );
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500 

    