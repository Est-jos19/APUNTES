import machine

class ALU:
    def __init__(self, PC, GPR) -> None:
        self.status = {'Z': 0}
        self.GPR = GPR
        self.PC = PC
        self.instr_set = self._instruction_set()
    #
    def _instruction_set(self):
        instr_set = {'ADDL' : self.ADDL,
                     'ADDR' : self.ADDR,
                     'DEC'  : self.DEC,
                     'INC'  : self.INC,
                     'JMP'  : self.JMP,
                     'JMPIZ': self.JMPIZ,
                     'MOVL' : self.MOVL,
                     'MOVR' : self.MOVR,
                     'HALT' : self.HALT}
        #
        return instr_set
    #
    def ADDL(self, op1, op2):
        self.GPR[op1] += op2
        self.status['Z'] = 0 if self.GPR[op1] != 0 else 1
    #
    def ADDR(self, op1, op2):
        self.GPR[op1] += self.GPR[op2]
        self.status['Z'] = 0 if self.GPR[op1] != 0 else 1
    #
    def DEC(self, op1, _):
        self.GPR[op1] -= 1
        self.status['Z'] = 0 if self.GPR[op1] != 0 else 1
    #
    def INC(self, op1, _):
        self.GPR[op1] += 1
        self.status['Z'] = 0 if self.GPR[op1] != 0 else 1
    #
    def JMP(self, op1, _):
        self.PC = op1 - 1
        self.status['Z'] = 0
    #
    def JMPIZ(self, _, __):
        offset = 1 if self.status['Z']==1 else 0
        self.PC += offset
    #
    def MOVL(self, op1, op2):
        self.GPR[op1] = op2
        self.status['Z'] = 0
    #
    def MOVR(self, op1, op2):
        self.GPR[op1] = self.GPR[op2]
        self.status['Z'] = 0
    #
    def HALT(self, op1, op2):
        self.PC = -2
    #
    def exec(self, instr, op1, op2):
        func = self.instr_set[instr]
        func(op1, op2)
#
class MP(ALU):
    def __init__(self, program) -> None:
        self.PC = 0
        self.GPR = [0, 0, 0, 0]
        self.program = program
        ALU.__init__(self, self.PC, self.GPR)
    #
    def _fetch(self):
        self.IR = self.program[self.PC]
    #
    def _decode(self):
        self.mnemonic, L = self.IR.split(',')
        self.L = int(L)
        #
        self.IR = self.IR.strip()
        self.OPCODE, modifier = self.mnemonic.split(' ')
        self.modifier = int(modifier)
    #
    def _exec(self):
        self.exec(self.OPCODE, self.modifier, self.L)
        self.PC = self.PC + 1
    #
    def run(self):
        while self.PC>-1:
            self._fetch()
            self._decode()
            self._exec()
            print(f"PC: {self.PC}, GPR: {self.GPR}")
        #
        print("Program halt")
#
# def producto(x0, x1):
#     prog = [f'MOVL 0, {x0}',
#              'DEC 0, 0',
#             f'MOVL 1, {x1}',
#             f'ADDL 1, {x1}',
#              'DEC 0, 0',
#              'JMPIZ 0, 0',
#              'JMP 3, 0',
#              'HALT 0, 0']
#     #
#     return prog
#
def remontada ():
    prog = [f'ADDL 0, 100',
            'ADDL 0, 1',
            'DEC 0,0' ,
            'JMPIZ 0, 0',
            'JMP, 3, 0'
            
            
            
            
            
            ]
def main():
    code = remontada()
    processor = MP(code)
    processor.run()
#
if __name__=='__main__':
    main()
