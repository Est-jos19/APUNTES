from machine import Pin
import utime

class sensor:
    def __init__(self, pin_trigger, pin_echo):
        self.p = Pin(pin_trigger, Pin.OUT)
        self.pulso0 = Pin(pin_echo, Pin.IN)
        self.pulso1 = Pin(0, Pin.OUT)
        self.pulso2 = Pin(4, Pin.OUT)
        self.pulso3 = Pin(16, Pin.OUT)
        self.pulso4 = Pin(17, Pin.OUT)
        self.con1 = Pin(5, Pin.OUT)
        self.con2 = Pin(18, Pin.OUT)
        self.bu= Pin(23, Pin.OUT)
        self.count = 0
        self.cm = 0
        self.unidades = 0
        self.centenas = 0
        self.decenas = 0
        self.espiga = 1
        self.valle = 30000
        self.cuenta = 0
        self.state = 'E'
        self.p.value(1)
        self.almacen = utime.ticks_us()
        self.o=0
        
    def chamba(self, prim, seg, ter):
        self.con = 0
        self.conn = 11
        self.numeros = {0 : [0, 0, 0, 0], 1:[0, 0, 0, 1], 2:[0, 0, 1, 0], 3:[0, 0, 1, 1], 4:[0, 1, 0, 0], 5:[0, 1, 0, 1], 6:[0, 1, 1, 0],
           7:[0, 1, 1, 1], 8:[1, 0, 0, 0], 9:[1, 0, 0, 1], 10:[1, 0, 1, 0],11:[1,0,1,1]}
        self.controlador = {0: [0, 0], 1:[0,1], 2:[1,0], 3:[1, 1]}
        
        self.primm = self.numeros[prim]
        
        self.coon = self.controlador[self.con]
        
        self.pines(self.primm, self.coon)
        self.con += 1
        
        self.primm = self.numeros[seg]
        
        self.coon = self.controlador[self.con]
        
        self.pines(self.primm, self.coon)
        self.con += 1
        
        self.primm = self.numeros[ter]
        
        self.coon = self.controlador[self.con]
        
        self.pines(self.primm, self.coon)
        self.con += 1
        
        self.primm = self.numeros[self.conn]
        
        self.coon = self.controlador[self.con]
        
        self.pines(self.primm, self.coon)
    
    def pines(self, x, y):
        self.pulso1.value(x[-1])
        self.pulso2.value(x[-2])
        self.pulso3.value(x[-3])
        self.pulso4.value(x[-4])
        
        self.con1.value(y[0])
        self.con2.value(y[1])
        
        utime.sleep_us(5000)
        
  
    def distancia(self):
        while True:
            current_time = utime.ticks_us()
            elapsed_time = utime.ticks_diff(current_time, self.almacen)
            self.almacen = current_time

            if self.state == 'E':
                self.cuenta += elapsed_time
                if self.cuenta >= self.espiga:
                    self.cuenta = 0
                    self.state = 'V'
                    self.p.value(0)
            elif self.state == 'V':
                self.cuenta += elapsed_time
                if self.cuenta >= self.valle:
                    self.cuenta = 0
                    self.state = 'E'
                    self.p.value(1)
            else:
                self.cuenta = 0
                self.state = 'E'

            pulso = self.pulso0.value()

            if pulso == 1:
                self.count += 1
            elif self.count != 0 and pulso == 0:
                self.cm = 0.923 * self.count
                if self.cm <= 45:
                    print(round(self.cm, 1), 'cm')
                    if self.cm >= 10:
                        self.bu.value(1)
                    self.cm = self.cm*10
                    self.o=round(self.cm, 0)
                    self.unidades = self.o % 10
                    
                    self.decenas = (self.o // 10) % 10
                    
                    self.centenas = self.o // 100
                    
                    self.chamba(self.unidades, self.decenas, self.centenas)
                    print(self.unidades, self.decenas, self.centenas)
                    self.cm = 0
                    self.count = 0
                else:
                    print('Te pasaste, padrino')
                    self.unidades=10
                    self.decenas=0
                    self.centenas=0
                    self.chamba(self.unidades, self.decenas, self.centenas)
                    self.count = 0
                    self.cm = 0

def main():
    b = sensor(25, 14)
    b.distancia()

if __name__ == "__main__":
    main()