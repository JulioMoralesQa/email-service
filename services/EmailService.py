from decouple import config
from email.mime.multipart import MIMEMultipart
from flask import Blueprint, jsonify
import smtplib
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader, Template
import secrets
import string
from email import encoders
from email.mime.base import MIMEBase

class EmailService():

    #*@Description: Podemos generar un password aleatorio de letras y numeros.
    #?@Params [password_length:Integer] Es la longitud del password
    #?Returns: Password OK, "" Failed
    @classmethod
    def password_generator(self,password_length = 8):
        try:
            letters = string.ascii_letters
            digits  = string.digits

            alphabet = letters + digits
            password = ''
            for i in range(password_length):
                password += ''.join(secrets.choice(alphabet))
    
            return (password + 'pwd')
        except Exception as ex:
            print("Error al enviar email")
            print(ex)
            return "";

    @classmethod
    #* @description: Se construye el array que contiene toda la informacion del email a enviar
    def build_array_email(self, subject, path_html, destinatary, optional_array={}):
        try:
            # Crear el email
            email = MIMEMultipart()
            email['Subject'] = subject                # Asunto
            email["From"] = config('MAIL_USERNAME')   # Remitente
            email["To"] = ', '.join(destinatary)      # Destinatarios (separados por coma)

            # Configurar Jinja2 para cargar la plantilla desde el directorio
            env = Environment(loader=FileSystemLoader(config('TEMPLATE_EMAIL')))
            template = env.get_template(path_html)    # Cargar la plantilla HTML

            # Renderizar la plantilla con datos opcionales si los hay
            plantilla_html = template.render(optional_array)

            # Adjuntar el contenido HTML renderizado
            email.attach(MIMEText(plantilla_html, 'html'))

            return email

        except Exception as ex:
            print("Error al enviar email")
            print(ex)
            return []
        
    #*@Description: Con este servicio podremos enviar emails
    #?@Params [subject:text, path_html:text, destinatary:array]
    #?Algunos datos se encuentran en el archivo .env
    #?Returns: 200 OK, 500 Failed
    @classmethod
    def send_email(self,subject,path_html,destinatary, optional_array = []):
        print(config('MAIL_USERNAME'))
        try:
            email_data = EmailService.build_array_email(subject,path_html,destinatary,optional_array)

            if(len(email_data) == 0):
                return 500
            
            #? Procedimiento de envio de email con SSL, para que no sea spam
            with smtplib.SMTP_SSL(config('DOMAIN_EXTENSION'), config('MAIL_PORT')) as server:  # ENVIAR DESDE UN DOMINIO PERSONALIZADO.
                server.login(config('MAIL_USERNAME'), config('MAIL_PASSWORD'))
                server.sendmail(config('MAIL_USERNAME'),destinatary, email_data.as_string())
            return 200;

        except Exception as ex:
            print("Error al enviar email")
            print(ex)
            return 500
        
    
    #*@Description: Con este servicio podremos enviar emails
    #?@Params [subject:text, path_html:text, destinatary:array]
    #?Algunos datos se encuentran en el archivo .env
    #?Returns: 200 OK, 500 Failed
    @classmethod
    def send_email_pdf(self,subject,path_html,destinatary, bytes_pdf, name_pdf):
        try:
            
            email           = MIMEMultipart();
            email['Subject']= subject;                 #?  1.- Asunto (Subject) 
            email["From"]   = config('MAIL_USERNAME')  #?  2.- ¿Quien envìa? (From)
            email["To"]     = ''.join(destinatary)   #?  3.- ¿A quien(es) envìa? (To)

            #Cargando datos de pdf
            part = MIMEBase("application", "octet-stream")
            part.set_payload(bytes_pdf)
            part.add_header('Content-Transfer-Encoding', 'base64')
            part['Content-Disposition'] = 'attachment; filename="%s"' % name_pdf
            encoders.encode_base64(part)
            email.attach(part)

            #Cargando datos de template
            with open(config('TEMPLATE_EMAIL') + path_html , 'r') as f: #?  4.- Template HTML (plantilla_html)
                template    = Template(f.read())
            plantilla_html  = template.render()

            email.attach(MIMEText(plantilla_html, 'html'))

            #? Procedimiento de envio de email con SSL, para que no sea spam
            with smtplib.SMTP_SSL(config('DOMAIN_EXTENSION'), config('MAIL_PORT')) as server:  # ENVIAR DESDE UN DOMINIO PERSONALIZADO.
                server.login(config('MAIL_USERNAME'), config('MAIL_PASSWORD'))
                server.sendmail(config('MAIL_USERNAME'),destinatary, email.as_string())
            return 200;

        except Exception as ex:
            print("Error al enviar email")
            print(ex)
            return 500
        
         #*@Description: Con este servicio podremos enviar emails
    #?@Params [subject:text, path_html:text, destinatary:array]
    #?Algunos datos se encuentran en el archivo .env
    #?Returns: 200 OK, 500 Failed
    @classmethod
    def send_email_img(self,subject,path_html,destinatary, bytes_pdf, name_pdf):

        


        try:
            
            email           = MIMEMultipart();
            email['Subject']= subject;                 #?  1.- Asunto (Subject) 
            email["From"]   = config('MAIL_USERNAME')  #?  2.- ¿Quien envìa? (From)
            email["To"]     = ', '.join(destinatary)   #?  3.- ¿A quien(es) envìa? (To)

            #Cargando datos de template
            with open(config('TEMPLATE_EMAIL') + path_html , 'r') as f: #?  4.- Template HTML (plantilla_html)
                template    = Template(f.read())
            plantilla_html  = template.render()

            email.attach(MIMEText(plantilla_html, 'html'))

            archivo_adjunto = open(bytes_pdf, 'rb')

            #Cargando datos de pdf
            part = MIMEBase("application", "octet-stream")
            part.set_payload((archivo_adjunto).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % name_pdf)            
            email.attach(part)

            

            #? Procedimiento de envio de email con SSL, para que no sea spam
            with smtplib.SMTP_SSL(config('DOMAIN_EXTENSION'), config('MAIL_PORT')) as server:  # ENVIAR DESDE UN DOMINIO PERSONALIZADO.
                server.login(config('MAIL_USERNAME'), config('MAIL_PASSWORD'))
                server.sendmail(config('MAIL_USERNAME'),destinatary, email.as_string())
            return 200;

        except Exception as ex:
            print("Error al enviar email")
            print(ex)
            return 500