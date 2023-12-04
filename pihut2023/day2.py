from machine import Pin

pinZeroForLed = Pin(0, Pin.OUT)
green = Pin(25, Pin.OUT)

pinZeroForLed.value(1)
green.value(1)
print("Block LED on!")