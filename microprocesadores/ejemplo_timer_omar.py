from machine import Pin, SoftI2C, Timer
import ssd1306
#
class oled_driver:
    WIDTH = 128
    HEIGHT = 64
    LIM_SHIFT = 150
    SHIFT_LEFT = -1
    SHIFTH_RIGHT = 1
    def _init_(self):
        i2c = SoftI2C(scl = Pin(18), sda = Pin(19))
        #
        self.driver = ssd1306.SSD1306_I2C(self.WIDTH, self.HEIGHT, i2c)
        self.enable_scroll = False
        self.limit = 0
    #
    def display(self):
        timer = Timer(0)
        timer.init(mode = Timer.PERIODIC, period = 100, callback = self._isr_timer)
        msg = "Secuenciadores"
        self.driver.text(msg, 10, 20)
        self.driver.show()
        #
        self.reset_msg = False
        while 1:
            if self.reset_msg:
                msg = input("Escribe el nuevo mensaje: ")
                if len(msg)>14:
                    msg = msg[0:14]
                #
                self.driver.text(msg, 10, 20)
                self.driver.show()
                self.reset_msg = False
            #
            if self.enable_scroll:
                self.driver.scroll(self.SHIFT_LEFT, 0)
                self.driver.show()
                self.enable_scroll = False
    #
    def _isr_timer(self, timer):
        if self.limit < self.LIM_SHIFT:
            self.enable_scroll = True
            self.limit += 1
        else:
            self.limit = 0
            self.reset_msg = True
#
def main():
    oled = oled_driver()
    oled.display()
#
if _name_ == '_main_':
    main()