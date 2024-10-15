from machine import Pin
import time
#primer ejercicio de Fibo

state = 'pedir'


while 1:
    if state == 'pedir':
        s = [0, 1]
        k = int(input("Ponga cuantos elementos quiere que tenga la serie, solo se pueden poner numeros:"))
        state = 'calcular'
    if state == 'calcular':
        if len(s) < k:
            nuevo = s[-1] +s[-2]
            s.append(nuevo)
        else:
            print(s)
            state = 'pedir'
    time.sleep(.1)
            
            
        