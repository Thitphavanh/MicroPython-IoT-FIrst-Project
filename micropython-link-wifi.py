import network
wifi = 'Hery'
password = 'xxxxxxxx'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.scan()
wifilist = wlan.scan()

for w in wifilist:
    print(w[0].decode('utf-8'))


wlan.isconnected()

print(wifi)

wlan.connect(wifi, password)
print(wlan.isconnected())

if wlan.isconnected():
    print('connected')

wlan.ifconfig()
