import time
from machine import Pin,ADC

class converterADC:
    def __init__(self,id=26):
        self.adc = ADC(Pin(id),atten = ADC.ATTN_6DB)
        self.state = 'read'
        
    def run(self):
        while 1:
            if self.state == 'read':
                val_int = self.adc.read_u16() #valor expresado en 16 bits
                val_uv = self.adc.read_uv()  #valor expresado en micro volts
                voltaje = (val_int * 0.000030518)
                #voltaje = (0.000001023 * val_uv) - 0.03763
                distancia = (voltaje * 18.519) + 8
                print(val_int, val_uv, voltaje, distancia)
                self.state = 'pause'
                
            else:
                self.state = 'read'
                time.sleep(.1)
                
def main():
    fsm = converterADC()
    fsm.run()
    
#
if __name__=='__main__':
    main()
    
            