from machine import Pin, I2C, ADC
from utime import sleep_ms
import ssd1306
import framebuf

class espirometro:
    
    def __init__ (self):
        self.adc = ADC(Pin(26), atten=ADC.ATTN_6DB)
        i2c = SoftI2C(scl = Pin(32), sda = Pin(33))
        self.driver = ssd1306.SSD1306_I2C(128, 64, i2c)
    
        self.tiempo = 19
        self.xlimit = [0, 128]
        self.ylimit = [0, 64]
        
        
    def conseguir_adc (self):
        val_int = self.adc.read_u16()
        val_uv = self.adc.read_uv() # en microvolts
        #pasar esos numeros de 16 bits al orden de los 90 leds disponibles
        #.2 volts para cada cuadrito 
        #self.cordy = 64 - val_uv // 500_000
        self.cordy = 6
        self.next = True
        
    def Display (self):
        
        if self.cordy in self.ylimit:
            self.driver.pixel(self.tiempo, self.cordy, 1)
            self.driver.show()
            self.tiempo += 1
            
            if self.tiempo == 128:
                self.tiempo -= 1
                self.cordy = 20
                self.driver.pixel(self.tiempo, self.cordy, 1)
                
    #def mover (self):
        #if
    def maquina(self):
        conseguir_adc()
        Display()
        
def main():
    oled = espirometro()
    oled.maquina()
if __name__ == '__main__':
    main()

        
        
        
        
            
            
        
        
        
        
                
        
        

