from machine import Pin
import utime

class UltrasonicSensor:
    def __init__(self, trigger_pin, echo_pin, salida_pins, control_pins):
        self.trigger_pin = Pin(trigger_pin, Pin.OUT)
        self.echo_pin = Pin(echo_pin, Pin.IN)
        self.salida_pins = [Pin(pin, Pin.OUT) for pin in salida_pins]
        self.control_pins = [Pin(pin, Pin.OUT) for pin in control_pins]
        self.cuenta = 0
        self.cm = 0
        self.espiga = 1000  # Cambiado a 1000 para milisegundos
        self.valle = 3000   # Asumiendo 3000 milisegundos
        self.state = 'E'
        self.trigger_pin.value(1)
        self.almacena = utime.ticks_ms()  # Cambiado a ticks_ms() para milisegundos
        self.control_disp = {0: [0,0], 1:[0,1], 2:[1,0], 3:[1,1]}
        # Diccionario de números binarios
        self.diccionario_binario = {
            0: '0000',
            1: '0001',
            2: '0010',
            3: '0011',
            4: '0100',
            5: '0101',
            6: '0110',
            7: '0111',
            8: '1000',
            9: '1001'
        }

    def estado_E(self, elapsed_time):
        self.cuenta += elapsed_time
        if self.cuenta >= self.espiga:
            self.cuenta = 0
            self.state = 'V'
            self.trigger_pin.value(0)

    def estado_V(self, elapsed_time):
        self.cuenta += elapsed_time
        if self.cuenta >= self.valle:
            self.cuenta = 0
            self.state = 'E'
            self.trigger_pin.value(1)

    def estado_default(self):
        self.cuenta = 0
        self.state = 'E'

    def distancia(self):
        actual = utime.ticks_ms()  # Cambiado a ticks_ms() para milisegundos
        tiempo = utime.ticks_diff(actual, self.almacena)
        self.almacena = actual

        if self.state == 'E':
            self.estado_E(tiempo)
        elif self.state == 'V':
            self.estado_V(tiempo)
        else:
            self.estado_default()

        pulso = self.echo_pin.value()

        if pulso == 1:
            self.cuenta += 1
        elif self.cuenta != 0 and pulso == 0:
            distancia = self.cuenta * 0.017  # Conversión a centímetros
            self.codificar_binario(distancia)
            self.cuenta = 0

    def codificar_binario(self, distancia):
        # Obtener decenas, unidades y decimales
        decenas = int(distancia) // 10
        unidades = int(distancia) % 10
        decimales = int((distancia - int(distancia)) * 10)

        # Barrido a través del diccionario y asignación al arreglo binario
        binario = []
        for i in range(4):
            if i == 0:
                valor = decimales
            elif i == 1:
                valor = unidades
            elif i == 2:
                valor = decenas
            else:
                valor = 0  # Si el contador está en 3, no hay valor para asignar
            binario.extend(self.diccionario_binario[valor])

        # Enviar valor binario a los pines de salida
        for i, pin in enumerate(self.salida_pins):
            pin.value(int(binario[i]))

    def control_contador(self):
        self.llaves = self.contro_disp.keys()
        for i in self.llaves :
            self.control_pin_vec = self.control_disp[i]
            self.control_pin_menos_sig = self.control_pin_vec[0]
            self.contro_pin_mas_sig = self.control_pin_vec[1]
        

    def run(self):
        while True:
            self.control_contador()
            self.distancia()

def main():
    sensor = UltrasonicSensor(25, 14, [0, 4, 16, 17], [5, 18])
    sensor.run()

if __name__ == "__main__":
    main()