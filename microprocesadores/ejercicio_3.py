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
    if state == 'sumar':
        count += 1
        if count >= desp:
            count = 0
            if num < TOP:
                num += 1
            elif num >= TOP:
                num = 0
            print(num)
    
    if state == 'sumar':
        if PB == 0:
            PB_2 += 1
            if PB_2 ==  BP_top:
                state = 'restar'
                PB_2 = 0
            else:
                state = 'sumar'
        if PB == 1:
            PB_2
    if state == 'restar':
        count += 1
        if count >= desp:
            count = 0
            if num > 0:
                num -= 1
            elif num <= 0:
                num = TOP
            print(num)                   
    if state == 'restar':
        if PB == 0:
            PB_2 += 1
            if PB_2 >= BP_top:
                state = 'sumar'
                PB_2 = 0
            else:
                state = 'restar'
    
    time.sleep_ms(1)

            