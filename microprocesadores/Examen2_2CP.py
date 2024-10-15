#Examen 2
import time
class exam2:
    
    def __init__(self):
        self.CP = 0
        # tengo que definir mi memoria, usare numeros de 3 cifras para poder especificar la literal, donde se guardara y que accion se hara
        #la centena es la litera, decena el lugar donde se guarda, y unidad la instruccion
        #ejemplo: 410 la instruccion es un 0, corresponde a un load, en el GPR 1, va a cargar un 4
        # para ek JMP hay que especificar a donde se quiere dar el salto
        # cargo un 5 y le aumento un (suma)
        #self.memoria = [5, 00, 4, 01 ]
        #loop para 2*10 = 20, 20 es el condiconal que si se cumple sigue en CP+= 1
        #self.memoria = [2, 00, 2, 01 ,20,04 ]
        #promedio de 8 numeros
        
        #promedio de 8 numeros
        #self.memoria = [2, 20, 3, 21, 4, 21, 56, 21, 87, 21, 34, 21, 13, 21, 4, 21 , 3,23]
        ## primeros 100 numeros
        self.memoria  = [1, 00, self.CP +1, 01, 5050, 04]
        
        
        self.GPR0 = int(0)
        self.GPR1 = int()
        self.GPR2 = int()
        self.GPR3 = int()
        self.registros = ["GPR0", "GPR1", "GPR2", "GPR3"]
        self.alu = [self.Load, self.Addl, self.Dec, self.Srr, self.Jmp, self.Jmpz ]
        self.CP = 0
        x= int()
        
    #en las instrucciones la literal es x
    def carga(self, x):
        self.literal = self.memoria[self.CP]
        self.CP += 1
            
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
        
    def Jmp(self, x, registro):	#direc = 4
    
        
        if self.registro == x:
            self.CP += 1
        elif self.registro < x:
            self.CP -= 3
    def Jmpz(self, _, registro):		#direc = 5
        if self.registro == 0:
            self.CP += 2
        else:
            self.CP += 1
            
    def run(self):		
        while 1:
            self.carga(self.CP)
            registro = (self.memoria[self.CP] // 10) % 10
            
            instruccion = self.memoria[self.CP] % 10
            
            instruccione = self.alu[instruccion]
            
            registro = self.registros[registro]
            instruccione(self.literal, registro )
            
            time.sleep(.01)
            
            if self.CP >= len(self.memoria):
                break
            
def main():
    width = exam2()
    width.run()
if __name__ == '__main__':
    main()              
    