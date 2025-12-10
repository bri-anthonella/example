from machine import Pin 
import time 

led_uno = Pin(12, Pin.OUT)

led_uno.on()
time.sleep(1)
led_uno.off()
time.sleep(1)

led_uno = Pin(13, Pin.OUT)

led_uno.on()
time.sleep(1)
led_uno.off()
time.sleep(1)

led_uno = Pin(18, Pin.OUT)

led_uno.on()
time.sleep(1)
led_uno.off()
time.sleep(1)

led_uno = Pin(19, Pin.OUT)

led_uno.on()
time.sleep(1)
led_uno.off()
time.sleep(1)
