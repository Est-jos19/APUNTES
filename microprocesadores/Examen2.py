#Examen 2
import time
class exam2:
    
    def __init__(self):
        # tengo que definir mi memoria, usare numeros de 3 cifras para poder especificar la literal, donde se guardara y que accion se hara
        #la centena es la litera, decena el lugar donde se guarda, y unidad la instruccion
        #ejemplo: 410 la instruccion es un 0, corresponde a un load, en el GPR 1, va a cargar un 4
        # para ek JMP hay que especificar a donde se quiere dar el salto
        self.memoria = [500, 401, 103,02,305, 304 , 511 ]
        self.GPR0 = int(0)
        self.GPR1 = int()
        self.GPR2 = int()
        self.GPR3 = int()
        self.registros = ["GPR0", "GPR1", "GPR2", "GPR#"]
        self.alu = [self.Load, self.Addl, self.Dec, self.Srr, self.Jmp, self.Jmpz ]
        self.CP = 0
    #en las instrucciones la literal es x
    def Load(self, x, registro): # direc 0
        
        self.registro = x
        print(registro, self.registro)
        self.CP += 1
        
    def Addl(self, x, registro):  #direc = 1
        self.registro += x
        
        print(registro, self.registro)
        self.CP += 1
        
    def Dec(self, _, registro):	#hay que especificar cuanto quiere que se decrezca
          
        self.registro -= 1
        print(registro, self.registro)
        self.CP += 1
        
        
    def Srr(self, x, registro):	#direc = 3
        self.registro = self.registro >> x
        print(registro, self.registro)
        self.CP += 1
        
    def Jmp(self, x, _):	#direc = 4
        self.CP = x
        
    def Jmpz(self, _, registro):		#direc = 5
        if self.registro == 0:
            self.CP += 2
        else:
            self.CP += 1
            
    def run(self):		
        while 1:
            
            literal = self.memoria[self.CP] // 100
            #print(literal)
            registro = (self.memoria[self.CP] // 10) % 10
            #print(registro)
            instruccion = self.memoria[self.CP] % 10
            #print(instruccion)
            instruccione = self.alu[instruccion]
            #print(instruccione)
            registro = self.registros[registro]
            instruccione(literal, registro )
            #print(registro)
            time.sleep(1)
            
            if self.CP >= len(self.memoria):
                break
            
def main():
    width = exam2()
    width.run()
if __name__ == '__main__':
    main()              
    
