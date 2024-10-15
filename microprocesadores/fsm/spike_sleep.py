import time
from machine import Pin

MAX_COUNT = 1000
MAX_CYCLES = 10
led = Pin(2, Pin.OUT)

count = -1
cycle = 0
state = 'spikes'
value = 0
led.value(value)
while 1:
    count += 1
    if count>=MAX_COUNT:
        state = 'spikes'
        count = -1
        cycle = 0
    else:
        if state=='spikes':
            if cycle<MAX_CYCLES:
                if count%50 == 0:
                    value ^= 1
                    led.value(value)
                    cycle += 1
            else:
                state = 'sleep'
                led.value(value)
                value = 0
                cycle = 0
        #
        elif state=='sleep':
            pass
        #
        else:
            state = 'spikes'
            count = -1
            cycle = 0
            value = 0
    #          
    time.sleep_ms(1)
