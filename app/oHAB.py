from openhab import openHAB
from time import sleep
from app import socketio


def sendMes(): 
    socketio.emit('message', {'data': 'works'})
    socketio.sleep(0)
    #socketio.on('myevent')
    return 
    
base_url = 'http://192.168.1.2:8080/rest'
openhab = openHAB(base_url)

def checkSTATE():
    items = openhab.fetch_all_items()
    sensor = items.get('LED1')
    sensorSTATE = sensor.state
    if (sensorSTATE=="OFF"):
        return 1
    else:
        return 0

def dummy():

    return 1