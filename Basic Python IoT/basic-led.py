from machine import Pin
import time
led = Pin(23, Pin.OUT)
led.on() # turn on led
led.off() # turn off led
for i in range(40):
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)