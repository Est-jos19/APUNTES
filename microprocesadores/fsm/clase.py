import utime
from machine import Pin

class debouncer:
    def __init__(self, top):
        self.state = 'UP'
        self.top = top
        self.out = 0
        self.start = utime.ticks_ms()
        self.pin = Pin(26, Pin.IN)
    #
    def up(self):
        self.out = 0
        if self.pin.value()==0:
            self.state = 'P'
            self.start = utime.ticks_ms()
    #
    def press(self):
        stop = utime.ticks_ms()
        diff = utime.ticks_diff(stop, self.start)
        if diff>self.top:
            self.out = 1
            self.state = 'UP'
            self.start = 0
    #
    def reset(self):
        self.state = 'UP'
        self.start = 0
        self.out = 0
    #
    def run(self):
        states = {'UP': self.up,
                  'P': self.press,
                  'reset': self.reset}
        while 1:
            if self.state in ('UP', 'P'):
                func = states[self.state]
            #
            else:
                func = states['reset']
            #
            func()
##
def main():
    fsm = debouncer(100_000)
    fsm.run()
#
if __name__=='__main__':
    main()