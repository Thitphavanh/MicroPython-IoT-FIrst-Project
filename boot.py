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
    lcd.putstr('WiFi:disconnected')
    
html = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Hugo 0.84.0">
    <title>ESP32 - Status</title>
    <link rel="canonical" href="https://getbootstrap.com/docs/5.0/examples/pricing/">
  <link href="https://getbootstrap.com/docs/5.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  </head>
  <body>
  <div class="container">
  <form>
    <center>
      <img src="https://raw.githubusercontent.com/UncleEngineer/MicroPython-IoT/main/light-bulb-on.png" width="300">
     <h3>LED 1</h3>
          <button  class="btn btn-primary" name="LED" value="ON" type="submit">ON</button>&nbsp;
        <button  class="btn btn-danger" name="LED" value="OFF" type="submit">OFF</button>
    </center>
   </form>
  </div>
  </body>
</html>
'''

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
    
    client.send(html)
    client.close()

