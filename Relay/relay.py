from machine import Pin
relay = Pin(23,Pin.OUT)
relay.value(1)
led = Pin(22,Pin.OUT)

led.on()
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
