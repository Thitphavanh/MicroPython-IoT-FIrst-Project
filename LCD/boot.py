from machine import Pin, SoftI2C
from i2c_lcd import I2cLcd
import time

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)
# print(i2c.scan())
# print('Address:',hex(i2c.scan()[0]))
lcd = I2cLcd(i2c, 0x27, 2, 16)

# string
lcd.move_to(3, 0)
lcd.putstr('MFC VS LFC')

# CHAR from ROM
# lcd.putchar(chr(92))

# Custom Char 0-7
'''
lcd.clear()
a = '         Hello'
b = '   Hello World'

lcd.putstr(a)
time.steel(2)
lcd.clear()
lcd.putstr(b)
'''

four = bytearray([0x00, 0x02, 0x06, 0x0A, 0x1F, 0x02, 0x00, 0x00])
semi = bytearray([0x00, 0x0E, 0x0E, 0x00, 0x0E, 0x0E, 0x00, 0x00])
zero = bytearray([0x00, 0x1F, 0x11, 0x11, 0x11, 0x1F, 0x00, 0x00])


lcd.custom_char(0, four)
lcd.custom_char(1, semi)
lcd.custom_char(2, zero)

lcd.move_to(6, 1)
lcd.putstr(chr(0))
# move to column 2 row 0
lcd.putstr(chr(1))
lcd.putstr(chr(2))

'''
lcd.blink_cursor_on()
time.sleep(5)
lcd.blink_cursor_off()
lcd.hide_cursor() # lcd.show_cursor()




# display on/off
for i in range(10):
    lcd.backlight_on()
    time.sleep(2)
    lcd.backlight_off()
    time.sleep(2)
'''
