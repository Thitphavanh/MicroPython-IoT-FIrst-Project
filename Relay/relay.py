from machine import Pin
import time
relay = Pin(23, Pin.OUT)
relay.off()

relay.value(0)
relay.value(1)
relay.value(0)
relay.value(1)

relay.value(0)
relay.value(1)

def relay_on():
    relay.value(0)
    print('LED : ON')

def relay_off():
    relay.value(1)
    print('LED : OFF')

relay_on()
# LED: ON
relay_off()
# LED: OFF
