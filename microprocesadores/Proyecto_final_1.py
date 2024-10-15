from machine import Pin, SoftI2C, ADC, Timer
import utime
import ssd1306 
import framebuf


class proyecto:
    def __init__(self):
        self.adc = ADC(Pin(34), atten=ADC.ATTN_6DB)
        i2c = SoftI2C(scl = Pin(32), sda = Pin(33))
        self.driver = ssd1306.SSD1306_I2C(128, 64, i2c)
        
        self.xlim = range(127)
        self.ylim = 64
        self.scroll = False
        self.tiempo = 1
        self.val_uv = 0
        self.cordy = 0
        self.next = False
        #self.cordy = 63        
    def display(self):
        while 1:
#             val_uv = self.adc.read_uv()
#             val_16 = self.adc.read_u16()
#             self.cordy = 63 - val_uv // 31_250
#             print(self.cordy)
#             self.start_ticks = utime.ticks_us()
#             
# #             timer = Timer(0)
#             periodo = utime.ticks_diff(utime.ticks_us(), self.start_ticks)
# #             timer.init(mode = Timer.PERIODIC, period = 1, callback = self.scrolling)
#             
#             val_uv = self.adc.read_uv()
#             val_16 = self.adc.read_u16()
#             self.cordy = 63 - val_uv // 30_600
#             print(val_uv)
            #timer3 = Timer(3)
            #timer3.init(mode = Timer.PERIODIC, period = 1, callback = self.next_pixel)
           
            if self.tiempo in self.xlim:
                val_uv = self.adc.read_uv()
                val_16 = self.adc.read_u16()
                self.cordy = 63 - val_uv // 30_600
                print(val_uv)
                self.driver.pixel(self.tiempo, self.cordy, 1)
                self.driver.show()
                self.tiempo += 1
            
            else:
                
                self.scroll = True
                if self.scroll:
                    self.driver.scroll(-1, 0)
                    self.driver.show()
                    self.tiempo -= 1
                    self.scroll = False
                
                
                
                
                
                  
    def scrolling(self):
        #timer3 = Timer(3)
        #timer3.init(mode = Timer.PERIODIC, period = 1, callback = self.next_pixel)
        if self.scroll:
            self.driver.scroll(-1, 0)
            self.driver.show()
            self.tiempo -= 1
            self.scroll = False
            
            #self.next = True
            
        
#     def maquina(self):
#         timer2 = Timer(1)
#         timer2.init(mode = Timer.PERIODIC, period = 1, callback = self.display) 
#         
                
                
            
def main():
    oled = proyecto()
    oled.display()
            
if __name__ == '__main__':
    main()  