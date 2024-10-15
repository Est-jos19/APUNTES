from machine import Pin
import time
#acomodar 3 numeros de mayor a menor
s = []
fibo = list()
state = 'pedir'
while 1:
    if state == 'pedir':
        
        x = int(input("Inserte un número:  "))
        s.append(x)
        
        if len(s) == 3:
            
            state = 'acomodar'
    if state == 'acomodar':
        print(s)
        if s[0] > s[1]:
            if s[0] > s[2]:
                fibo.append(s[0])
                if s[2] > s[1]:
                    fibo.append(s[2])
                    fibo.append(s[1])
                   
                elif s[1] > s[2]:
                    fibo.append(s[1])
                    fibo.append(s[2])
            
        elif s[1] > s[0]:
            if s[1] > s[2]:
                fibo.append(s[1])
                if s[2] > s[0]:
                    fibo.append(s[2])
                    fibo.append(s[0])
                elif s[0] > s[2]:
                    fibo.append(s[0])
                    fibo.append(s[2])
    
        print(fibo)
        del(s)
        
        s = []
        state = 'pedir'
    time.sleep(1)
                
                
                