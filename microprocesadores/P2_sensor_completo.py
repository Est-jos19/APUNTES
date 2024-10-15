#Práctica 2. Sistema de alarma para evitar colisiones en una silla de ruedas autónoma
#Alumnos: José Estrada Rodríguez
#         Misael de Jesús Contreras Ramírez
#         Angel Vera Vázquez
#UEA: Secuenciadores y Microprocesadores
#Profesor: Omar Piña Ramírez
from machine import Pin, ADC 
import utime 

class sensor:
    def _init_(self, pin_trigger, pin_echo):
        # Configuración de pines de entrada y salida
        self.p = Pin(pin_trigger, Pin.OUT)
        self.pulso0 = Pin(pin_echo, Pin.IN)
        # Definición de pines de control
        self.pulso1 = Pin(0, Pin.OUT) #Pin de control de bits
        self.pulso2 = Pin(4, Pin.OUT) #Pin de control de bits
        self.pulso3 = Pin(16, Pin.OUT) #Pin de control de bits
        self.pulso4 = Pin(17, Pin.OUT) #Pin de control de bits
        self.con1 = Pin(5, Pin.OUT) #Pin para controlar los anodos en la basys
        self.con2 = Pin(18, Pin.OUT) #Pin para controlar los anodos en la basys
        self.bu = Pin(32, Pin.OUT) #Pin para el buzzer
        # Inicialización de variables
        self.count = 0
        self.cm = 0
        self.unidades = 0
        self.centenas = 0
        self.decenas = 0
        self.espiga = 1
        self.valle = 30000
        self.cuenta = 0
        self.state = 'E'
        self.p.value(1)  # Establece el pin de disparo en alto
        self.almacen = utime.ticks_us()  # Almacena el tiempo actual en microsegundos
        self.o = 0
        self.adc = ADC(Pin(26), atten=ADC.ATTN_6DB)  # Configura el ADC para leer el pin 26 con atenuación de 6dB
        
    def chamba(self, prim, seg, ter):  # Método para controlar los pines de salida
        # Definición de diccionarios para controlar los pines
        self.numeros = {0: [0, 0, 0, 0], 1: [0, 0, 0, 1], 2: [0, 0, 1, 0], 3: [0, 0, 1, 1], 4: [0, 1, 0, 0], 5: [0, 1, 0, 1], 6: [0, 1, 1, 0],
                        7: [0, 1, 1, 1], 8: [1, 0, 0, 0], 9: [1, 0, 0, 1], 10: [1, 0, 1, 0], 11: [1, 0, 1, 1]}
        self.controlador = {0: [0, 0], 1: [0, 1], 2: [1, 0], 3: [1, 1]}
        
        self.primm = self.numeros[prim]  # Obtiene el patrón de pines para el primer dígito
        self.coon = self.controlador[self.con]  # Obtiene el controlador correspondiente
        
        self.pines(self.primm, self.coon)  # Llama al método para establecer los pines de salida
        self.con += 1  # Incrementa el contador de controladores
        
        # Repite el proceso para los siguientes dígitos
        # (segundo y tercer dígito)
        
    def pines(self, x, y):  # Método para establecer los pines de salida
        # Establece los pines de salida según el patrón proporcionado
        self.pulso1.value(x[-1])
        self.pulso2.value(x[-2])
        self.pulso3.value(x[-3])
        self.pulso4.value(x[-4])
        
        # Establece los pines de control según el controlador proporcionado
        self.con1.value(y[0])
        self.con2.value(y[1])
        
        utime.sleep_us(5000)  # Espera breve
        
    def distancia(self):  # Método para medir la distancia
        while True:  # Inicia MEF
            current_time = utime.ticks_us()  # Obtiene el tiempo actual en microsegundos
            elapsed_time = utime.ticks_diff(current_time, self.almacen)  # Calcula el tiempo transcurrido
            self.almacen = current_time  # Actualiza el tiempo en almacen
            
            val_int = self.adc.read_u16()  # Lee el valor analógico del sensor (expresado en 16 bits)
            voltaje = (val_int * 0.000030518)  # Convierte el valor a voltaje
            distancia = (voltaje * 18.519) + 8  # Convierte el voltaje a distancia y se suman 8 por el trimpot
            
            # Control de pulso para activar el trigger
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
            
            pulso = self.pulso0.value()  # Lee el valor del pin de echo
            
            if pulso == 1:  # Si hay un pulso
                self.count += 1  # Incrementa el contador de pulsos
            elif self.count != 0 and pulso == 0:  # Si no hay pulso y el contador no es cero
                self.cm = 1.1923 * self.count + .6  # Calcula la distancia en centímetros
                if self.cm <= distancia:  # Si la distancia es menor o igual que la medida del sensor
                    print(round(distancia, 1), 'cm')# Imprime la distancia
                    if self.cm <= 10:
                        self.bu.value(1)
                    else:
                        self.bu.off()
                    # Divide la distancia en unidades, decenas y centenas
                    self.cm = self.cm * 10
                    self.o = round(self.cm, 0)
                    self.unidades = self.o % 10
                    self.decenas = (self.o // 10) % 10
                    self.centenas = self.o // 100
                    self.chamba(self.unidades, self.decenas, self.centenas)# Llama al método para controlar los pines según los dígitos
                    self.cm = 0  # Reinicia la variable de distancia
                    self.count = 0  # Reinicia el contador de pulsos
                else:  # Si la distancia es mayor que la medida del sensor
                    print(round(distancia, 1), 'cm') # Imprime la distancia
                    self.unidades = 10  # Marca la distancia como mayor que el sensor
                    self.decenas = 0
                    self.centenas = 0
                    # Llama al método para controlar los pines según los dígitos
                    self.chamba(self.unidades, self.decenas, self.centenas)
                    self.count = 0  # Reinicia el contador de pulsos
                    self.cm = 0  # Reinicia la variable de distancia
                    self.bu.off()

def main():  
    b = sensor(25, 14)  
    b.distancia()  

if _name_ == "_main_":
    main()  