try:
    import urequests as requests
except ImportError:
    import requests
from machine import Pin
import time
def getvar():
    DEVICE = "device name"
    VARIABLE1 = "variable name"
    pin14 =  Pin(14, Pin.OUT, value=1)
    TOKEN = "default token"
    url = "http://things.ubidots.com/api/v1.6/devices/" + DEVICE + "/" + VARIABLE1 + "/lv?token=" + TOKEN
    while True:

        light1 = requests.get(url)
        print ("Channel 1 is now : " + light1.text)
        if light1.text == "1.0":
	        pin14.off()
        elif light1.text == "0.0":
	        pin14.on()
        time.sleep(1)