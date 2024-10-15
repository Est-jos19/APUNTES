## ejercicio 3
from machine import Pin
import time
PBVALUE  = Pin(14, Pin.IN)
#PB = PBVALUE.value()
BP_top = 1500
desp = 1000
state = 'sumar'
num = 0
TOP = 187
count = 0
#PB
PB_2 = 0

while 1:
    PB = PBVALUE.value()
    if PB == 0:
        num += 1
    print(num)
    
    time.sleep(1)