from machine import Pin, SoftI2C
from utime import sleep_ms
from ssd1306 import SSD1306_I2C
import framebuf

class oled_driver:
    WIDTH = 128
    HEIGHT = 64
    def __init__ (self):
        i2c = SoftI2C(scl = Pin(18), sda = Pin(19))
        #
        self.driver = ssd1306.SSD1306_I2C(self.WIDTH, self.HEIGHT, i2c)
        
def main():
    oled = oled_driver()
    oldec.driver.text('Hola mundo', 0,0)
    oled.driver.show()
    
if __name__ = '__main__':
    main()