import time
from machine import Pin

def transition(vstates, state):
    vstate = vstates.get(state)
    value = vstate['value']
    top = vstate['top']
    state = vstate['next']
    return value, top, state

led = Pin(25, Pin.OUT)

vstates = {'pulse' : {'value' : 1, 'top' : 50, 'next' : 'sleep'},
          'sleep' : {'value' : 0, 'top' : 950,'next' : 'pulse'},
          'reset' : {'value' : 0, 'top' : 10, 'next' : 'pulse'}
          }
state = 'reset'
value, top, state = transition(vstates, state)
count = 0
led.value(value)

while  1:
    count += 1
    if count >=top:
        count = 0
        if state in ('pulse', 'sleep'):
            value, top, state = transition(vstates, state)
        else:
            value, top, state = transition(vstates, 'reset')
        #
        led.value(value)
    time.sleep_ms(1)
