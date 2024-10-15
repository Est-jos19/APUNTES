
    
from machine import Pin, SoftI2C, ADC, Timer
from utime import sleep_ms
import ssd1306 
import framebuf


class proyecto:
    def __init__(self):
        self.adc = ADC(Pin(34), atten=ADC.ATTN_6DB)
        i2c = SoftI2C(scl = Pin(32), sda = Pin(33))
        self.driver = ssd1306.SSD1306_I2C(128, 64, i2c)
        
        self.xlim = 128
        self.ylim = 64
        self.scroll = False
        self.tiempo = 1
        self.val_uv = 0
        self.cordy = 63
        self.state =  "adc"
        #self.cordy = 63
        
    def acd(self):
        val_int = self.adc.read_u16()
        val_uv = self.adc.read_uv()
        #self.cordy = 63 - self.val_uv // 31_250
        # en microvolts
        #pasar esos numeros de 16 bits al orden de los 90 leds disponibles
        #.2 volts para cada cuadrito 
        #self.cordy = 64 - val_uv // 500_000
        self.cordy = 6
        self.state = "display"
        
    def display(self):
        timer = Timer(0)
        #timer.init(mode = Timer.PERIODIC, period = 100, callback = self.scrolling)    
        if self.cordy < self.ylim:
            self.driver.pixel(self.tiempo, self.cordy, 1)
            self.driver.show()
            self.tiempo += 1
            if self.tiempo >= self.xlim-1:
                self.scroll = True
                self.state = "adc"
                
    def scrolling(self, timer):
        if self.scroll:
            self.driver.scroll(-1, 0)
            self.driver.show()
            self.enable_scroll = False
    def maquina(self):
        estados = {"adc": self.adc, "display": self.display }
        while 1:
            if self.state in ["adc"]:
                self.acd()
            if self.state in ["display"]:
                self.display()
                
                
            
def main():
    oled = proyecto()
    oled.display()
            
if __name__ == '__main__':
    main()