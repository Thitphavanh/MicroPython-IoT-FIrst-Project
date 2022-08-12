from machine import Pin, SoftI2C
from i2c_lcd import I2cLcd
from lcd_api import LcdApi
import time
import dht
import network
import socket


# LED
led = Pin(23, Pin.OUT)
led.off()

# LCD
i2c = SoftI2C(scl=Pin(22), sda = Pin(21), freq = 100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
time.sleep(1)
lcd.clear()

text = 'Starting...'
lcd.putstr(text)

# WIFI
wifi = 'Hery'
password = '44332211'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
time.sleep(2)
wlan.connect(wifi, password)
time.sleep(2)
status = wlan.isconnected()
ip, _, _, _ = wlan.ifconfig()

if status == True:
    lcd.clear()
    text = 'IP:{}'.format(ip)
    lcd.putstr(text)
    time.sleep(2)
    lcd.clear()
    lcd.putstr('Connected')
else:
    lcd.clear()
    lcd.putstr('WiFi: disconnected')
    
html = 'Hello World'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 80
s.bind((host, port))
s.listen(5)

while True:
    client, addr = s.accept()
    print('connection from:', addr)
    data = client.recv(1024).decode('utf-8')
    print([data])
