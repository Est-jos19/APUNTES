## con interrupcion

from machine import Pin, SoftI2C, ADC, Timer
import utime
import ssd1306

class Proyecto:
    def __init__(self):
        self.adc = ADC(Pin(34), atten=ADC.ATTN_6DB)
        i2c = SoftI2C(scl=Pin(32), sda=Pin(33))
        self.driver = ssd1306.SSD1306_I2C(128, 64, i2c)
        self.xlim = range(127)
        self.tiempo = 1
        self.last_update = utime.ticks_ms()
        self.val_volts = 0
        self.val_uv = 0

    def display(self):
        while True:
            current_time = utime.ticks_ms()
            if utime.ticks_diff(current_time, self.last_update) >= 2.5:  # 2500 us = 2.5 ms
                self.last_update = current_time
                self.val_uv = self.adc.read_uv()
                self.val_volts = self.val_uv / 1000000  # Convertir microvolts a volts
                timer =  Timer(0)
                timer.init(mode = Timer.PERIODIC, period = 1, callback = self.texto)
                
                if self.tiempo in self.xlim:
                    self.cordy = 63 - self.val_uv // 15625
                    self.driver.pixel(self.tiempo, self.cordy, 1)
                    self.driver.show()
                    self.tiempo += 1
                else:
                    self.driver.scroll(-1, 0)
                    self.driver.show()
                    self.tiempo -= 1

                self.driver.show()
                
    def texto(self, timer):
            
        if self.val_volts < 0.29:
            flujo_text = "Flujo Bajo"
        elif 0.3 <= self.val_volts <= 0.6 :
            flujo_text = "Flujo Medio"
        else:
            flujo_text = "Flujo Alto"
                    
        self.driver.fill_rect(0, 0, 128, 10, 0)
        self.driver.text(flujo_text, 0, 0)
        self.driver.show()
            
            
            

def main():
    oled = Proyecto()
    oled.display()

if __name__ == '__main__':
    main()