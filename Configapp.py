from decouple import config


class Configapp:
    SECRET_KEY = config('SECRET_KEY')


class DevelopmentConfig(Configapp):
    DEBUG = 'OFF'


Configapp = {
    'development': DevelopmentConfig
}