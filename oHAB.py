from openhab import openHAB
from time import sleep
from app import app
from socketIO_client import SocketIO, LoggingNamespace



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
    with SocketIO('http://localhost', 5000, LoggingNamespace) as socketIO:
        socketIO.emit('messagecs','Take plate from left cupboard')
        sleep(7)
        socketIO.emit('messageps','Previous Step: Take plate from left cupboard')
        socketIO.emit('messagecs','Refill and turn on kettle')
        sleep(7)
        socketIO.emit('messageps','Previous Step: Refill and turn on kettle')
        socketIO.emit('messagecs','Take butter from fridge')

    return 1