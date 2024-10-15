import utime
from machine import Pin

class measure:
    def __init__(self):
        self.state = 'low'
        self.start = utime.ticks_us()
        self.pin = Pin(26, Pin.IN)
    #
    def low(self):
        if self.value==1:
            self.state = 'high'
            self.start = utime.ticks_us()
    #
    def high(self):
        if self.value==0:
            stop = utime.ticks_us()
            width = utime.ticks_diff(stop, self.start)
            print(f'{width}')
            self.state = 'low'
            self.start = stop
    #
    def reset(self):
        self.state = 'low'
        self.start = 0
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
def main():
    width = measure()
    width.run()
#
if __name__ == '__main__':
    main()