from machine import Pin
import time 
pincero = Pin(25,  Pin.OUT)
pin1=Pin(26, Pin.OUT)
pin2=Pin(27, Pin.OUT)
pin3=Pin(14, Pin.OUT)
pin4 = Pin(33, Pin.OUT)
pin5 = Pin(12, Pin.OUT)


# contador de unidas a miles
numeros = {000_000_ : [0, 0,0,0], 100_000:[0,0,0,1], 200_000:[0,0,1,0], 300_000:[0,0,1,1], 400_000:[0,1,0,0], 500_000:[0,1,0,1],
           600_000:[0,1,1,0],
           700_000:[0,1,1,1], 800_000:[1,0,0,0], 900_000:[1, 0,0,1]} # diccionario de numeros
control_disp = {0: [0,0], 1:[0,1], 2:[1,0], 3:[1,1]} # diccionario para controlar los display
num= 0

con = 0

while 1:
    #poner la cuenta
    print(numeros[num])
    cont = numeros[num]
    pincero.value(cont[0])
    pin1.value(cont[1])
    pin2.value(cont[2])
    pin3.value(cont[3])
    num =+ 100_000
    if num == 1_000_000:
        num = 0
        
        #poner la cuenta
        decenas =+ 100_00
        if decenas == 1_000_00:
            decenas = 0
            # aumentar la cuenta
            
            centenas =+ 100_000
            if centenas == 1_000_000:
                centenas = 0
                #aumentar la cuenta
                
                
                if miles == 1_000_000:
                    miles = 0
    if con < 4: # controla los display
        control = control_disp[con]
        pin4.value(control[0])
        pin5.value(control[1])
        con += 1
        if con == len(control_disp):
            con = 0
time.sleep_(1_000_000)       
                
        