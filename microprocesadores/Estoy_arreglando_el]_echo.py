#hacer el trigger

import utime
from machine import Pin


class Practica:
    
    def __init__(self):
        self.estado = "Alto"
        self.value = 0
        self.pin_cero = Pin(25,Pin.OUT)
        self.pin_echo = Pin(14, Pin.IN)
        self.start_ticks = utime.ticks_us()
        self.duracion = 0
        self.start_echo = 0
        self.count = 0
        
    def Bajo(self):
        
        
        self.pin_cero.off()
        self.duracion = 0
        #print ("Esta en bajo")
        periodo = utime.ticks_diff(utime.ticks_us(), self.start_ticks)
        if periodo >= 120_00:
            
            self.start_ticks = utime.ticks_us()
            self.estado = "Alto" 
    def Alto (self):
        
        self.pin_cero.on()
        #print ("Esta en alto")
        periodo = utime.ticks_diff(utime.ticks_us(), self.start_ticks)
        
        if periodo >= 10000:
           self.start_ticks = utime.ticks_us()
           self.estado = "Echo" 
                
            
    ## ahora a leer el echo
    def Echo(self):
        pin_e = self.pin_echo.value()
        
        
        if pin_e == 1:
            self.start_echo = utime.ticks_us()
            self.count += 1
            #print(self.count)
        elif pin_e == 0  :
            #self.end_echo = utime.ticks_us()
            #self.duracion = utime.ticks_diff(self.end_echo, self.start_echo)
              
            print (self.count)
            self.count = 0
            self.estado = "Bajo"
        else :
           print("No hay nada")
           
    #def Despliegue
            
    def run (self):
        estados = {"Bajo": self.Bajo ,"Alto": self.Alto, "Echo": self.Echo}
        while 1:
            
            if self.estado in ("Bajo", "Alto", "Echo"):
                func = estados[self.estado]
            
            else : func =estados["reset"]
        
            func()
            
            
def main():
    width = Practica()
    width.run()
if __name__ == '__main__':
    main() 


        
    