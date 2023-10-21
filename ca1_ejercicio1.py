from gpiozero import Button
from datetime import datetime

#Establecemos boton en el GPIO2
button = Button(2)

#Creamos y abrimos el documento
with open("botonRegistro.txt", "a") as documentoBoton: 

#Ciclo para comprobar estado del boton
    while True:
        fechaActual = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        if button.is_pressed:
            data =  f"{fechaActual} --> Boton presionado\n"
            documentoBoton.write(data)
        