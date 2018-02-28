from openhab import openHAB

base_url = 'http://192.168.1.2:8080/rest'
openhab = openHAB(base_url)
oldsensor = 0
  # fetch all items
items = openhab.fetch_all_items()
sensor = items.get('LED1')
sensorSTATE = sensor.state
if (sensorSTATE == "OFF"):
    print("OFF")
