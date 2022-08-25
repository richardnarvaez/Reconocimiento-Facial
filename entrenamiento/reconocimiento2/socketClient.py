import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def sendEvent(data):
    print('message received with ', data)
    sio.emit('rv', {'response': data})

@sio.event
def disconnect():
    print('disconnected from server')

def conectarse():
    sio.connect('http://localhost:3000/')
    sendEvent("Hola usuario")
