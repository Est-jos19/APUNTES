from machine import Pin
import utime
#
p = Pin(25, Pin.OUT)
pulso0 = Pin (14, Pin.IN)
count = 0
cm=0
espiga = 1
valle = 3000
cuenta = 0
state = 'E'
p.value(1)
#
while 1:
    
    if state == 'E':
        cuenta += 1
        if cuenta >= espiga:
            cuenta = 0
            state = 'V'
            p.value(0)
    #
    elif state == 'V':
        cuenta += 1
        if cuenta >= valle:
            cuenta = 0
            state = 'E'
            p.value(1)
    #
    else:
        cuenta = 0
        state = 'E'
    #
    pulso = pulso0.value()
    if pulso == 1:
        count += 1
    elif count != 0 and pulso == 0:
        cm=0.597*count
        if cm<= 45:
            print(round(cm,2), 'cm')
            cm=0
            count = 0
        else:
            print('te pasaste padrino')
            count=0
            cm=0
    utime.sleep_us(1)