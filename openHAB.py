from openhab import openHAB

base_url = 'http://prankit.gupta@brl.ac.uk:openHAB1an@35.177.18.86/rest'
openhab = openHAB(base_url)
oldsensor = 0
  # fetch all items
items = openhab.fetch_all_items()
print(items)
