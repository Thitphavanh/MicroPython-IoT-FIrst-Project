import socket
import network
import time
from machine import Pin

serverip = '178.128.125.82'
port = 9000


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
print(wlan.isconnected())
