import time
from machine import Pin

class spike:
    def __init__(self, top):
        self.top = top
        self.vstates = {'pulse': {'value': 1, 'top':  50, 'next': 'sleep'},
                        'sleep': {'value': 0, 'top': 950, 'next': 'pulse'},
                        'reset': {'value': 0, 'top':  10, 'next': 'pulse'}}
        #
        self.led = Pin(2, Pin.OUT)
        #
        self.stage = 'reset'
        self.value, self.top, self.stage = self.transition()
        self.count = 0
        self.led.value(self.value)
    #
    def transition(self):
        vstate = self.vstates.get(stage)
        value = vstate['value']
        top = vstate['top']
        stage = vstate['next']
        return value, top, stage
    #
    def run(self):
        while 1:
            self.count += 1
            if self.count>=self.top:
                self.count = 0
                if self.stage in ('pulse', 'sleep'):
                    self.value, self.top, self.stage = self.transition()
                else:
                    self.value, self.top, self.stage = self.transition()
                #
                self.led.value(self.value)
            #
            time.sleep_ms(1)
#
def main(top):
    spike_inst = spike(top)
    spike_inst.run()
#
if __name__ == '__main__':
    main()