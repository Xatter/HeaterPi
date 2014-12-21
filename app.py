import cherrypy
import os

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
on_button = 11
off_button = 13

GPIO.setup(off_button, GPIO.OUT)
GPIO.setup(on_button, GPIO.OUT)

import smbus
bus = smbus.SMBus(0)
address = 0x60

class HeaterController:
    exposed = True
    def GET(self):
        temperature = bus.read_byte_data(address, 1)
        return str(temperature)

    def POST(self):
        GPIO.output(off_button, 1)
        time.sleep(1)
        GPIO.output(off_button, 0)

    def PUT(self):
        GPIO.output(on_button, 1)
        time.sleep(1)
        GPIO.output(on_button, 0)

class Root:
    heater = HeaterController()

    @cherrypy.expose
    def index(self):
        f = open('app/index.html')
        return f.readlines()


def config():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    config = {}
    config['/'] = {
        'tools.staticdir.root': os.path.join(current_dir, 'app'),
        'tools.gzip.on': True,
    }

    # TODO: Move this config into BetaRegistration Class
    for path in ['heater']:
        config['/' + path] = {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher()
        }

    for path in ['scripts', 'styles', 'views', 'images', 'vendor']:
        config['/' + path] = {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': path
        }

    return config

cherrypy.config.update({
    'server.socket_host':'0.0.0.0',
    'server.socket_port':int(os.environ.get('PORT','80')),
    'log.error_file':'error.log',
    'log.screen': True
})

cherrypy.quickstart(Root(), '/', config=config())
