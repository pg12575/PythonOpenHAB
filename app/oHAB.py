from openhab import openHAB
from time import sleep
from app import app
from socketIO_client import SocketIO, LoggingNamespace

   
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
       
        #socketIO.emit('messagecs','Take plate from left cupboard')
        #sleep(7)
        #socketIO.emit('messageps','Previous Step: Take plate from left cupboard')
        #socketIO.emit('messagecs','Refill and turn on kettle')
        #sleep(7)
        #socketIO.emit('messageps','Previous Step: Refill and turn on kettle')
        #socketIO.emit('messagecs','Take butter from fridge') 

        items = openhab.fetch_all_items()
        sensor = items.get('LED1')
        sensorSTATE = sensor.state
        counter = 0
        checker = 0
        while True:
            items = openhab.fetch_all_items()
            sensor = items.get('LED1')
            sensorSTATE = sensor.state

            if ((sensorSTATE=="OFF") & ((checker==0) | (counter==0))):
                if (counter>0):
                    socketIO.emit('messageps','Previous Step: Turn Lights Off')    
                socketIO.emit('messagecs','Say "Alexa, All Lights On"')
                checker = 1
                counter = counter + 1
            elif ((sensorSTATE=="ON") & ((checker==1) | (counter==0))):
                if (counter>0):
                    socketIO.emit('messageps','Previous Step: Turn Lights On')  
                socketIO.emit('messagecs','Say "Alexa, All Lights Off"')
                checker = 0
                counter = counter + 1
            sleep(1)

    return 1



def dummy2():
    with SocketIO('http://localhost', 5000, LoggingNamespace) as socketIO:  
        
        socketIO.emit('messagecs','Take plate from left cupboard')
        sleep(7)
        socketIO.emit('messageps','Previous Step: Take plate from left cupboard')
        socketIO.emit('messagecs','Refill and turn on kettle')
        sleep(7)
        socketIO.emit('messageps','Previous Step: Refill and turn on kettle')
        socketIO.emit('messagecs','Take butter from fridge') 

    return 2