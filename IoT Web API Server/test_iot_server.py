from machine import Pin
import network
import time
import socket
import _thread
import dht

import urequests
import json


wifi = 'DESKTOP-ABSKJM8 9024'
password = '123456789'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
time.sleep(2) # delay 2 seconds
wlan.connect(wifi, password)
time.sleep(2)
status = wlan.isconnected() # True/False
ip ,_ ,_ ,_ = wlan.ifconfig()

print(ip)

# DHT22
d = dht.DHT22(Pin(23))
t = 0
h = 0

def check_temp():
    print('check temp starting...')
    global t
    global h
    while True:
        try:
            d.measure()
            time.sleep_ms(2000) #millisec
            t = d.temperature()
            h = d.humidity()
            print('DHT22:', t, h)
            time.sleep_ms(5000)
        except:
            pass

def post_temp():
    while True:
        try:
            url = 'http://192.168.137.190:8000/api'
            data = {'code': 'TM-101','title':'Temp1','temperature':t, 'humidity':h}

            #r = urequests.post(url, data=json.dumps(data))
            r = urequests.post(url, json=data)
            result = json.loads(r.content)
            print(result)
            time.sleep(10)
        except:
            print('ERROR')
            
_thread.start_new_thread(check_temp,())
_thread.start_new_thread(post_temp,())