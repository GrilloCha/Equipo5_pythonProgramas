from gpiozero import Button
from time import sleep
from datetime import datetime

button = Button(2)

while True:
    documentoBoton = open("botonRegistro.txt", "a")
    fechaActual = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if button.is_pressed:
        data =  f"{fechaActual} --> Boton presionado"
        documentoBoton.write(data)
    documentoBoton.close()
    
    