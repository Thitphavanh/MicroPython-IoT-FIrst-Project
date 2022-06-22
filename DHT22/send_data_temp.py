import socket
import network
import time
from machine import Pin
import dht

serverip = '192.168.0.54'
port = 9002


def send_data(data):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.connect((serverip, port))
    server.send(data.encode('utf-8'))
    data_server = server.recv(1024).decode('utf-8')
    print('Server:', data_server)
    server.close()


wifi = 'Hery'
password = '44332211'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
time.sleep(2)
wlan.connect(wifi, password)
time.sleep(2)
print('STATUS : ', wlan.isconnected())

print('> Temperature checking...')
d = dht.DHT22(Pin(23))

for i in range(50):
    d.measure()
    time.sleep(1)
    temp = d.temperature()
    humid = d.humidity()
    print(temp)
    print(humid)
    # text = 'TEMP-HUMID:{} and {}'.format(temp,humid)
    text = 'Status:{}'.format(temp)
    send_data(text)
    time.sleep(3)
    print('-------')


# d = dht.DHT22(Pin(23))
# d.measure()
# print(d.temperature())

# print(d.humidity())


# for i in range(100):
#     d.measure()
#     time.sleep(1)
#     print(d.temperature())
#     print(d.humidity())
#     print('------')
#     time.sleep(3)
