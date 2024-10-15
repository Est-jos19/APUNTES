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
           self.estado = "Bajo" 
                
            
    ## ahora a leer el echo
    def Echo(self, pin_e):
        
        
        
        if pin_e == 1:
            self.start_echo = utime.ticks_us()
            self.count += 1
            #print(self.count)
        else:
            if self.start_echo !=0:
                duracion = utime.ticks_diff(utime.ticks_us(), self.start_ticks)
                if duracion > 0:
            #self.end_echo = utime.ticks_us()
            #self.duracion = utime.ticks_diff(self.end_echo, self.start_echo)
                    cm = duracion * 0.000597
                    cm  = round(duracion)
                    print (cm)
                    self.start_echo= 0
                    self.estado = "Bajo"
        
           
    #def Despliegue
            
    def run (self):
        estados = {"Bajo": self.Bajo ,"Alto": self.Alto}
        while 1:
            
            if self.estado in ("Bajo", "Alto"):
                func = estados[self.estado]
            
            else : func =estados["reset"]
        
            func()
            self.Echo(self.pin_echo.value())
            
            
def main():
    width = Practica()
    width.run()
if __name__ == '__main__':
    main() 