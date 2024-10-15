from machine import Pin, ADC, SoftI2C, Timer
import ssd1306

class ventilador:
    WIDTH = 128
    HEIGHT = 64
    def __init__(self):
        i2c = SoftI2C(scl=Pin(13), sda=Pin(25))
        self.driver = ssd1306.SSD1306_I2C(self.WIDTH, self.HEIGHT, i2c)
        self.adc = ADC(Pin(27), atten=ADC.ATTN_2_5DB)
        self.prom = 0
        self.valor = 0
        self.msg = 'Apagado'
        self.val_uv = 0
        self.x = 35
        self.count = 0
        timer = Timer(0)
        timer2 = Timer(1)
        timer.init(mode = Timer.PERIODIC, period = 10, callback = self.muestra)
        timer2.init(mode = Timer.PERIODIC, period = 100, callback = self.offset)
        
    def offset(self,timer2):
        pos = 62 - self.valor//468770
        self.driver.pixel(127,pos,1)
        self.driver.show()
        self.driver.scroll(-1,0)
        
    def muestra(self, timer):
        self.val_uv = self.adc.read_uv()
        self.prom += self.val_uv
        self.count += 1
        if self.count >= 100:
            self.valor = self.prom//100
            print(self.valor)
            self.prom = 0
            self.count = 0

        
    def promedio(self):
        if self.valor >= 66500:
            self.msg = 'Flujo Bajo'
            self.x = 23
        
        if self.valor >= 300000:
            self.msg = 'Flujo Medio'
            self.x = 19
            
        if self.valor > 495000:
            self.msg = 'Flujo Alto'
            self.x = 23
            
        if self.valor < 66500:
            self.msg = 'Apagado'
            self.x = 35
            
    def despliegue(self):
        #self.driver.fill(0)
        #self.driver.text(self.msg, self.x, 27)
        #self.driver.show()
        pass
        
    def run(self):
        while 1:
            self.promedio()
            self.despliegue()
            
def main():
    fsm = ventilador()
    fsm.run()
    
if __name__ == '__main__':
    main()