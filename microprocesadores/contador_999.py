# contador para 3 displays
from machine import Pin
import time 
pincero = Pin(25,  Pin.OUT)
pin1=Pin(26, Pin.OUT)
pin2=Pin(27, Pin.OUT)
pin3=Pin(14, Pin.OUT)
pin4 = Pin(33, Pin.OUT)
pin5 = Pin(12, Pin.OUT)
count = 0 
numeros = {0 : [0, 0,0,0], 1:[0,0,0,1], 2:[0,0,1,0], 3:[0,0,1,1], 4:[0,1,0,0], 5:[0,1,0,1], 6:[0,1,1,0],
           7:[0,1,1,1], 8:[1,0,0,0], 9:[1, 0,0,1], 10:[1,0,1,0], 11:[1,0,1,1], 12:[1,1,0,0], 13:[1,1,0,1], 14:[1,1,1,0],
           15:[1,1,1,1]}
control_disp = {0: [0,0], 1:[0,1], 2:[1,0], 3:[1,1]}
num= 0
decenas  = 1
centenas = 1
con = 0

state = 'unidades'
while 1:
    # hacer el contador para tenga un efecto de cascad
    # con tres estados puedo intercambiar muy rapido entre estados
    if state == 'unidades':
        
        cont = numeros[num]
        pincero.value(cont[0])
        pin1.value(cont[1])
        pin2.value(cont[2])
        pin3.value(cont[3])
        
        control = control_disp[0]
        pin4.value(control[0])
        pin5.value(control[1])
        
        num += 1
        
        if num >= len (numeros):
            
            state = 'decenas'
            num = 0
        
    elif state == 'decenas':
          dec = numeros[decenas]
          pincero.value(dec[0])
          pin1.value(dec[1])
          pin2.value(dec[2])
          pin3.value(dec[3])
          
          control = control_dip[1]
          pin4.value(control[0])
          pin5.value(control[1])
          
          
          if decenas < len(numeros):
             state = 'unidades'
             decenas += 1
          elif decenas >= len (numeros):
                state = 'centenas'
    elif state == 'centenas':
         cent = numeros[centenas]
         pincero.value(dec[0])
         pin1.value(dec[1])
         pin2.value(dec[2])
         pin3.value(dec[3])
          
         control = control_dip[2]
         pin4.value(control[0])
         pin5.value(control[1])
         
         if centenas < len (numeros):
             state = 'unidades'
             centenas += 1
         elif centenas >= len(numeros):
             num = 0
             decenas = 0
             centenas = 0
        
    time.sleep_ms(1)
        
        