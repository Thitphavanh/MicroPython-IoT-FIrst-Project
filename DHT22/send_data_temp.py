from machine import Pin
import dht
import time

d = dht.DHT22(Pin(23))
d.measure()
print(d.temperature())

print(d.humidity())


for i in range(100):
    d.measure()
    time.sleep(1)
    print(d.temperature())
    print(d.humidity())
    print('------')
    time.sleep(3)
