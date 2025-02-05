from flask import Blueprint, jsonify, request, make_response
from decouple import config
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
       
        response        = EmailService.send_email("Solicitud de Información", 'ventas@cormago.com.mx', "templateContactoCormago.html", "ventas@cormago.com.mx", data);
        
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
        params=(1,datasig,config('SECRET_KEY_PG'))
        storeProcedure="\"LaPerlaWeb\".\"EmailOperations_encrypted\""
        note_data   = StandardModel.standar_query(storeProcedure,params)
        
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
        message = data['message']

        if message == "suscripcion":
            asunto = "Nueva suscripcion al Newsletter"
        else:
            asunto = "Solicitud de Informacion"
       
        response        = EmailService.send_email_gafimex(asunto,"contacto@gafimex.com","3G8tss955..","smtp.zoho.com", "templateGafimex.html", "contacto@gafimex.com", data);
        
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
        data_json = json.dumps([data])
        user_email = data['email']
        user_name = data['firstname']

        validation_params = (2, data_json, config('SECRET_KEY_PG'))  # Usa opción 2 para validación
        validation_proc = "\"GafimexWeb\".\"EmailOperations_encrypted\""
        validation_response = StandardModel.standar_query(validation_proc, validation_params)

        # Verifica si el procedimiento almacenado indica que el email ya existe
        if validation_response and validation_response.get('exists', False):
            return jsonify(
                message=f"El email {user_email} ya está registrado en la base de datos.",
                category="error",
                status=400
            )

        # Si el email no existe, procede con la inserción y el envío del correo
        if user_name == "newsletter":
            template = "templateSubscriptionGafimex.html"
        else:
            template = "templateSubscriptionGafimexDiscount.html"

        params=(1,data_json,config('SECRET_KEY_PG'))
        storeProcedure="\"GafimexWeb\".\"EmailOperations_encrypted\""
        note_data   = StandardModel.standar_query(storeProcedure,params)
        print("linea 53")
        print(note_data)
       
        response        = EmailService.send_email_gafimex("Confirmacion Suscripcion","contacto@gafimex.com", "3G8tss955..",'smtp.zoho.com', template, user_email);
        
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
        servicio = data['servicio']

        if servicio == "Suscripcion Descuento":
            asunto = "Nueva suscripcion al Newsletter"
        else:
            asunto = "Cotizacion de servicio"
       
        response        = EmailService.send_email(asunto, 'ventas@cormago.com.mx', "templateCotizacion.html", "ventas@cormago.com.mx", data);
        
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
        # Extraer datos del JSON enviado
        data = request.json['data']
        data_json = json.dumps([data])
        user_email = data['email']
        user_name = data['firstname']

        # Validar si el email ya existe en la base de datos
        validation_params = (2, data_json, config('SECRET_KEY_PG') )  # Usa opción 2 para validación
        validation_proc = "\"CormagoWeb\".\"EmailOperations_encrypted\""
        validation_response = StandardModel.standar_query(validation_proc, validation_params)

        # Verifica si el procedimiento almacenado indica que el email ya existe
        if validation_response and validation_response.get('exists', False):
            return jsonify(
                message=f"El email {user_email} ya está registrado en la base de datos.",
                category="error",
                status=400
            )

        # Si el email no existe, procede con la inserción y el envío del correo
        if user_name == "newsletter":
            template = "templateSubscriptionCormago.html"
        else:
            template = "templateSubscriptionCormagoDiscount.html"

        params = (1, data_json,config('SECRET_KEY_PG'))
        storeProcedure = "\"CormagoWeb\".\"EmailOperations_encrypted\""
        note_data = StandardModel.standar_query(storeProcedure, params)

        # Enviar email
        email = MIMEMultipart()
        email['info'] = 'Gracias por suscribirte a la perla'
        email['option'] = 'html'
        response = EmailService.send_email(
            "Confirmación de suscripción", 
            'ventas@cormago.com.mx', 
            template, 
            user_email
        )

        return jsonify(
            message=('Error al enviar email', 'Email enviado correctamente')[response == 200],
            category="success",
            data=response,
            status=200,
            registros=format(1)
        )
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500



    