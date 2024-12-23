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
       
        response        = EmailService.send_email("Solicitud de Informacion", 'ventas@cormago.com.mx', "templateContactoCormago.html", "ventas@cormago.com.mx", data);
        
        return jsonify(
            message     = ('Error al enviar email','Email enviado correctamente')[response == 200],
            category    = "success",
            data        = response,
            status      = 200,
            registros   = format(1)
        );
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
@main.route('/send-email-hyvecode', methods=['POST'])
def send_email_hyvecode():
    
    
    try:
        
        data= request.json['data']
       
        response        = EmailService.send_email_hyvecode("Solicitud Informacion","contacto@hyvecode.com.mx","0X@787LV{w/y*d","mail.hyvecode.com.mx", "templateContactoHyvecode.html", "jcontacto@hyvecode.com.mx", data);
        
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
        response        = EmailService.send_email_la_perla("ConfirmacionEmail", "la-perla-newsletter@revistalaperla.com", "1J7JlAic54k0{",'smtp.zoho.com', "templateRevistaLaPerla.html", data, email);
        
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
       
        response        = EmailService.send_email_gafimex("Solicitud Informacion","contacto-gafimex@gafimex.com","5c3krM6iDuOy{","smtp.zoho.com", "templateGafimex.html", "contacto-gafimex@gafimex.com", data);
        
        return jsonify(
            message     = ('Error al enviar email','Email enviado correctamente')[response == 200],
            category    = "success",
            data        = response,
            status      = 200,
            registros   = format(1)
        );
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500 
    
@main.route('/save-email-gafimex', methods=['POST'])
def saveMailGafimex():
    
    
    try:
        
        data= request.json['data']
        sig = [{"email":data}]
        datasig= json.dumps(sig)
        params=(1,datasig)
        storeProcedure="\"GafimexWeb\".\"EmailOperations\""
        note_data   = StandardModel.standar_query(storeProcedure,params)
        print("linea 53")
        print(note_data)
       
        response        = EmailService.send_email_gafimex("Confirmacion Suscripcion","contacto-gafimex@gafimex.com", "5c3krM6iDuOy{",'smtp.zoho.com', "templateSubscriptionGafimex.html", data);
        
        return jsonify(
            message     = ('Error al enviar email','Email enviado correctamente')[response == 200],
            category    = "success",
            data        = response,
            status      = 200,
            registros   = format(1)
        );
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/cotizacion-cormago', methods=['POST'])
def cotizacion_cormago():
    
    
    try:
        
        data= request.json['data']
       
        response        = EmailService.send_email("Cotizacion de Servicio", 'ventas@cormago.com.mx', "templateCotizacion.html", "ventas@cormago.com.mx", data);
        
        return jsonify(
            message     = ('Error al enviar email','Email enviado correctamente')[response == 200],
            category    = "success",
            data        = response,
            status      = 200,
            registros   = format(1)
        );
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/save-email-cormago', methods=['POST'])
def saveMailCormago():
    
    
    try:
        
        data= request.json['data']
        sig = [{"email":data}]
        datasig= json.dumps(sig)
        params=(1,datasig)
        storeProcedure="\"CormagoWeb\".\"EmailOperations\""
        note_data   = StandardModel.standar_query(storeProcedure,params)
        print("linea 53")
        print(note_data)
        email           = MIMEMultipart();
        email['info']   = 'Gracias por suscribirte a la perla';
        email['option'] = 'html';
        response        = EmailService.send_email("Confirmacion de suscripcion", 'ventas@cormago.com.mx', "templateSubscriptionCormago.html", data);
        
        return jsonify(
            message     = ('Error al enviar email','Email enviado correctamente')[response == 200],
            category    = "success",
            data        = response,
            status      = 200,
            registros   = format(1)
        );
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

    