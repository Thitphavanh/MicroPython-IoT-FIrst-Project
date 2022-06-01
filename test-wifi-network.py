import network


wifi = 'Hery'
password = '44332211'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.scan()
wifilist = wlan.scan()
for w in wifilist:
    print(w[0].decode('utf-8'))

wlan.isconnected()
print(wifi)
print(password)

wlan.connect(wifi,password)
print(wlan.isconnected())

if wlan.isconnected():
    print('connected')

wlan.ifconfig()
print(wlan.isconnected())

import socket
serverip = '192.168.0.54'
port = 9000
def send_data(data):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.connect((serverip, port))
    server.send(data.encode('utf-8'))
    data_server = server.recv(1024).decode('utf-8')
    print('Server:', data_server)
    server.close()

send_data('Hello PC')
send_data('LED-ON')
send_data('LED-OFF')

from machine import Pin

led = Pin(23, Pin.OUT)

led.on()
send_data('LED1: ON')

led.off()
send_data('LED1: OFF')

import urequests
url = 'http://uncle-machine.com/hello/'
result = urequests.get(url)
print(result.text)

# result = urequests.get(url='http://uncle-machine.com/api/hello')
# urequests.get(url='http://uncle-machine.com/hello/').text