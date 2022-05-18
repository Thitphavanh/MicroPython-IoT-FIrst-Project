from machine import Pin
import time

led = Pin(23, Pin.OUT)
led.on()
led.off()
for i in range(50):
	led.on()
	time.sleep(1)
	led.off()
	time.sleep(1)
