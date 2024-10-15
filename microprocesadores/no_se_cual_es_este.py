## progrma para muestreo
from machine import Pin, ADC
import time
class triger ():
    
    def __init__ (self):
        self.estado = 'no_pico'
        self.tiempo = 100_000
        self.tiempo_alto = 1_000
        self.count = 0
        self.value = 0
        self.pin_out = Pin (25, Pin.OUT)
        self.pin_in = Pin (14, Pin.IN)
    def no_pico(self):
        
        self.tiempo = 100_000
        self.valor_t = self.value
        print("estamos en cero")
        self.count += 1
        if self.count >= self.tiempo:
            self.count = 0
            self.estado = 'pico'
            
    def pico(self):
    
        self.tiempo = 1_000
        self.valor_t = not(self.value)
        print ("estamos en uno")
        self.count += 1
        if self.count >= self.tiempo_alto:
            self.estado = 'no_pico'
            self.count = 0
    def reset(self):
        self.state = "Bajo"
        self.count = 0
    def run(self):
        #vamos a cambiar de estados.
        estados = {"pico": self.pico ,"no_pico": self.no_pico, "reset" : self.reset}
        while 1:
            if self.estado in ("pico", "no_pico"):
                func = estados[self.estado]
            
            else : func =estados["reset"]
        
            func()
            self.pin_out.value(self.value)
        
            time.sleep_ms(1)
        #self.echo = self.pin_in.value()
def main():
    width = triger()
    width.run()
#
if __name__ == '__main__':
    main()
        
            
        
        
            
            
    #def pico (self):
        
        
        