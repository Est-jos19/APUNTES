import utime
from machine import Pin

class measure:
    RESOLUTION = 5 #us
    def __init__(self):
        self.state = 'low'
        self.count = 0
        self.pin = Pin(26, Pin.IN)
    #
    def low(self):
        if self.value==1:
            self.state = 'high'
            self.count = 0
    #
    def high(self):
        self.count + 1
        if self.value==0:
            width = self.count * measure.RESOLUTION
            print(f'{width}')
            self.state = 'low'
    #
    def reset(self):
        self.state = 'low'
        self.count = 0
    #
    def run(self):
        fsm = {'low': self.low,
               'high': self.high,
               'reset': self.reset}
        #
        while 1:
            self.value = self.pin.value()
            if self.state in ('low', 'high'):
                func = fsm[self.state]
            #
            else:
                func = fsm['reset']
            #
            func()
            #
            utime.sleep_us(measure.RESOLUTION)
#
def main():
    width = measure()
    width.run()
#
if __name__ == '__main__':
    main()