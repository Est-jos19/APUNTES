#hacer el trigger

import utime
from machine import Pin

pin_cero = Pin(25, Pin.OUT)
pin_in = Pin(14, Pin.IN)
class Practica:
    
    def __init__(self):
        self.estado = "Bajo"
        self.value = 0
        self.pin_cero = Pin(25,Pin.OUT)
        self.pin_in = Pin(14, Pin.IN)
        self.start_ticks = utime.ticks_us()
        self.cm = 0
        self.count = 0
        
        
    def Bajo(self):
        self.estado  = "Bajo"
        
        self.pin_cero.off()
        
        #print ("Esta en bajo")
        periodo = utime.ticks_diff(utime.ticks_us(), self.start_ticks)
        if periodo >= 120_0:
            
            self.start_ticks = utime.ticks_us()
            self.estado = "Echo" 
    def Alto (self):
        
        self.pin_cero.on()
        #print ("Esta en alto")
        
        periodo = utime.ticks_diff(utime.ticks_us(), self.start_ticks)
        if periodo >= 1_0:
            self.start_ticks = utime.ticks_us()
            self.estado = "Bajo"
    def run (self):
        estados = {"Bajo": self.Bajo ,"Alto": self.Alto, "Echo" : self.Echo}
        while 1:
            if self.estado in ("Bajo", "Alto", "Echo"):
                func = estados[self.estado]
            
            else : func =estados["Bajo"]
            
            
            func()
            
            
            
    def Echo (self):
        
        self.pin_en = self.pin_in.value()
        if self.pin_en == 1:
            self.count += 1
        elif self.pin_en == 0 and self.count != 0:
            self.cm = self.count * .923
            if self.cm <=45:
                print (self.cm, "cm")
                self.count = 0
                self.estad0 = "Bajo"
            else :
                print ("Distancia no valida")
                self.count=0
                self.estado = ""
            
def main():
    width = Practica()
    width.run()
if __name__ == '__main__':
    main() 
