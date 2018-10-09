import network
import time
count = 0
ssid = "your ssid"
password = "your pass"
station = network.WLAN(network.STA_IF)
def connect():
    global station
    global count	
    if station.isconnected() == True:	
        print("Already connected")
        return
    a = False
    while (not a) and (count <= 5):
        a = connectwifi()
def connectwifi():
    print("connecting...")
    global count
    global ssid
    global password
    global station
    station.active(True)
    station.connect(ssid, password)
    time.sleep(7)
    if station.isconnected() == False:
        count = count + 1
        return False
    print("Connection successful")
    print(station.ifconfig())
    return True
	