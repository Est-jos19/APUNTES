## practica 2, puslo cuadrado y medicion con clases
from machine import Pin, ADC
import utime

## clase para pulso cuadrado
pi_out = Pin(25, Pin.OUT)
pin_in = Pin (14, Pin.IN)
# para que me de mi frecuencia de multiplexion debo usar 2 ms de periodo, osea un segundo muestra y otro no
class MuestreoCuadrado:
    
    def __init__ (self):
        self.state = "Bajo"
        self.count = 0
        self.pin_out = Pin (25, Pin.OUT)
        self.pin_in = Pin (14, Pin.IN)
        self.pinuno = Pin(15, Pin.OUT)
        self.pindos = Pin(26, Pin.OUT)
        self.pintres = Pin(27, Pin.OUT)
        self.pincuatro = Pin(14, Pin.OUT)
        self.pin5 = Pin(33, Pin.OUT)
        self.pin6 = Pin(12, Pin.OUT)
        self.contador = 0
        self.cm = 0
        self.disp = 0
        self.numeros = {0 : [0, 0,0,0], 1:[0,0,0,1], 2:[0,0,1,0], 3:[0,0,1,1], 4:[0,1,0,0], 5:[0,1,0,1], 6:[0,1,1,0],
           7:[0,1,1,1], 8:[1,0,0,0], 9:[1, 0,0,1]}
        self.control_disp = {0: [0,0], 1:[0,1], 2:[1,0], 3:[1,1]}
        self.num= 0
        self.cont = 0
        self.start = utime.ticks_us()
    
    def contador(self):
        self.numeros = {0 : [0, 0,0,0], 1:[0,0,0,1], 2:[0,0,1,0], 3:[0,0,1,1], 4:[0,1,0,0], 5:[0,1,0,1], 6:[0,1,1,0],
           7:[0,1,1,1], 8:[1,0,0,0], 9:[1, 0,0,1]}
        self.control_disp = {0: [0,0], 1:[0,1], 2:[1,0], 3:[1,1]}
        self.num= 0
        self.cont = 0
        
    def Bajo(self):
        
        if self.rest < 10000:
            self.value = 0
            self.pin_out.value(self.value)
            self.echo  = self.pin_in.value()
        elif self.rest >= 10000 :
            self.start = utime.ticks_us
            self.rest = 0
            self.state = "Alto"

            
                    
    def Alto(self):
        self.value = 1
        self.count += 1
        self.pin_out.value(self.value)
        self.echo = self.pin_in.value()
        print("hay un uno")
        if self.count >= 1:
            self.count = 0
            
            stop = utime.ticks_us()
            width = utime.ticks_diff(stop, self.start)
            self.state = "Bajo"
    def reset(self):
        self.state = "Bajo"
        self.count = 0
        
    def imprimir(self):
        
        if self.echo == 1:
           self.contador += 1
        elif self.contador != 0 and self.echo == 0:
            ## haccerlo en forma de decenas y dejar prendido el led de punto decimal
            self.cm=597*self.contador
            self.contador = 0
            if self.cm >= 40: print("Te pasaste")
            print (self.cm)
    def asig_disp (self):
        self.pinuno.value(self.display[0])
        self.pindos.value(self.display[1])
        self.pintres.value(self.num_disp[0])
        self.pincuatro.value(self.num_disp[1])
        self.pin5.value(self.num_disp[2])
        self.pin6.value(self.num_disp[3])
    def Display (self):
        self.unidades = self.cm % 10
        self.decenas = (self.cm // 10)%10
        self.centenas  = self.cm // 100
        if self.cm <= 9:
            self.display  = self.control_disp[0]
            self.num_disp = self.numeros[self.unidades]
            self.asig_disp()
            
            #usar un display y los demas deben estar en cero
            #prender el led de punto decimal
        elif self.cm <= 99:
            self.display  = self.control_disp[0]
            self.num_disp = self.numeros[self.unidades]
            self.asig_disp()
            self.display  = self.control_disp[1]
            self.num_disp = self.numeros[self.decenas]
            self.asig_disp()
            
            #usar dos display y el tercer hacerlo cero
            #prender el bit de punto decimal
        elif self.cm <= 999:
            self.display  = self.control_disp[0]
            self.num_disp = self.numeros[self.unidades]
            self.asig_disp()
            self.display  = self.control_disp[1]
            self.num_disp = self.numeros[self.decenas]
            self.asig_disp()
            self.display  = self.control_disp[2]
            self.num_disp = self.numeros[self.centenas]
            self.asig_disp()
        
            #usar los 3 display y prender el led de punto decimal
        
    def run(self):
        fsm = {"Bajo": self.Bajo,
               "Alto": self.Alto,
               "reset": self.reset}
        while 1:
            
            if self.state in ("Bajo" , "Alto"):
                func = fsm[self.state]
            else : func = fsm[reset]
    
            func()
            
            
            self.imprimir()
            self.Display()
            
    
        
            #time.sleep_ms(1)
def main():
    width = MuestreoCuadrado()
    width.run()
#
if __name__ == '__main__':
    main()            
         
            
            
        
        