from machine import Pin
import time 
pincero = Pin(25,  Pin.OUT)
pin1=Pin(26, Pin.OUT)
pin2=Pin(27, Pin.OUT)
pin3=Pin(14, Pin.OUT)
pb = Pin(32, Pin.IN)
#disp2 = Pin(33, Pin.OUT)
## Una maquina de estado finito es una forma de modelar procesos.
## Estudiar UML para modelado de procesos
## inicia en cero y con cada ciclo de reloj  pone un uno o un cero 
numeros = {0 : [0, 0,0,0], 1:[0,0,0,1], 2:[0,0,1,0], 3:[0,0,1,1], 4:[0,1,0,0], 5:[0,1,0,1], 6:[0,1,1,0],
           7:[0,1,1,1], 8:[1,0,0,0], 9:[1, 0,0,1], 10:[1,0,1,0], 11:[1,0,1,1], 12:[1,1,0,0], 13:[1,1,0,1], 14:[1,1,1,0],
           15:[1,1,1,1]}
#display = {0:[0,0], 1:[0,1], 2:[1,0], 3:[1,1]}
num= 0
#basys = 0
#def control_disp(a, b):
 #   while 1:
  #      disp = display[basys]
   #     a = (disp[0])
    #    b = (disp[1])
     #   basys +=1
      #  time.sleep(.000001)
       # return a, b
        #if basys == len(display):
         #   basys=0
i = 0
top = 50
top2 = 950
state  = 'U'
est3 = 0
# FSM
espiga = Pin (25, Pin.OUT)
espiga.value(1)
while 1:
    print(numeros[num])
    cont = numeros[num]
    pincero.value(cont[0])
    pin1.value(cont[1])
    pin2.value(cont[2])
    pin3.value(cont[3])
    num+=1
    
    if num==len(numeros):
        num=0
        
    if state == 'U':
        
        i += 1
        
        if i >= top:
            state = 'D'
            i = 0
            espiga.value(0)
    elif state == 'D':
        i += 1
        
        if i >= top2:
            state = 'U'
            i = 0
            espiga.value(1)
    time.sleep(1)
    
        
    
    
        