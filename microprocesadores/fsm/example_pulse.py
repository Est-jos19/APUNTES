import time
from machine import Pin

def transition(vstates, stage):
    vstate = vstates.get(stage)
    value = vstate['value']
    top = vstate['top']
    stage = vstate['next']
    return value, top, stage

led = Pin(2, Pin.OUT)

vstates = {'pulse': {'value': 1, 'top':  50, 'next': 'sleep'},
           'sleep': {'value': 0, 'top': 950, 'next': 'pulse'},
           'reset': {'value': 0, 'top':  10, 'next': 'pulse'}}

stage = 'reset'
value, top, stage = transition(vstates, stage)
count = 0
led.value(value)
while 1:
    count += 1
    if count>=top:
        count = 0
        if stage in ('pulse', 'sleep'):
            value, top, stage = transition(vstates, stage)
        else:
            value, top, stage = transition(vstates, 'reset')
        #
        led.value(value)
    #
    time.sleep_ms(1)