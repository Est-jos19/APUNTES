## ejercicio 3
from machine import Pin
import time
PBVALUE  = Pin(14, Pin.IN)
#PB = PBVALUE.value()
PB_top = 1500
desp = 1000
state = 'suma'
num = 0
TOP = 18
count = 0

PB_2 = 0
state2 = 0


while 1:
    PB = PBVALUE.value()
    ## vamos a contar los 1.5 segundos
    
    if PB == 0:
        PB_2 += 1
        if state == 'resta':
            if PB_2 == PB_top:
                state = 'suma'
                state2 = 'next'
        elif state == 'suma':
            if PB_2 == PB_top:
                state = 'resta'
                state2 = 'next'
            
    elif state2 == 'next':
        PB_2 = 0
        
      #  print(PB_2)
        
    if state == 'suma':
        count += 1
        if count >= desp:
            count = 0
            if num < TOP:
                num += 1
            elif num >= TOP:
                num = 0
            print(num)
    if state == 'resta':
        count += 1
        if count >= desp:
            count = 0
            if num > 0:
                num -= 1
            elif num <= 0:
                num = TOP
            print(num)
    time.sleep_ms(1)

            
