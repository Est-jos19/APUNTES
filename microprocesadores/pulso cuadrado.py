import time
from machine import Pin

COUNT_7HZ  = 142857//2
#buscar frecuencia de 8.264 hz
# debe de haber 1 ms up y 120 ms down
COUNT_11HZ = 90909//2
pin_7hz  = Pin(25, Pin.OUT)
pin_11hz = Pin(26, Pin.OUT)
count_7 = 0
count_11 = 0
val_7 = 1
val_11 = 1
pin_7hz.value(val_7)
pin_11hz.value(val_11)

while 1:
    count_11 += 1
    count_7+= 1
    if count_7 >= COUNT_7HZ:
        count_7 = 0
        val_7 ^= 1
        pin_7hz.value(val_7)
    if count_11 >= COUNT_11HZ:
        count_11 = 0
        val_11 ^= 1
        pin_11hz.value(val_11)
        
    
    time.sleep_us(1)

            
    

    
    
