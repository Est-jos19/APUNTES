import machine
from machine import Pin, ADC, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import time



# Inicialización de la pantalla OLED
i2c = machine.I2C(scl=machine.Pin(21), sda=machine.Pin(22))
oled = SSD1306_I2C(128, 64, i2c)

# Configuración de la señal cuadrada
pin_señal = machine.Pin(14, machine.Pin.OUT)  # Configurar el pin de la señal como salida

# Función para generar la señal cuadrada y mostrarla en el OLED
def generar_y_mostrar_señal():
    estado = False
    while True:
        pin_señal.value(estado)  # Cambiar el estado del pin de la señal
        estado = not estado  # Alternar entre alto y bajo
        oled.fill(0)  # Limpiar la pantalla
        oled.text("guapo, poderoso, asombros", 0, 15)
        oled.text("muy precioso,", 0, 25)
        oled.text("armonioso", 0,35)
        oled.text("soy buen socio" , 0, 45)
        oled.hline(10, 60, 120, 1)
        oled.show()  # Mostrar el estado de la señal en la pantalla OLED
        time.sleep(1)  # Esperar 1 segundo entre cada cambio de estado

# Llamar a la función para generar y mostrar la señal
generar_y_mostrar_señal()