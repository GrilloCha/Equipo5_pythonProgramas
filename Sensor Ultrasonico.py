from gpiozero import DistanceSensor
from time import sleep
from datetime import datetime
import matplotlib.pyplot as plt

sensor = DistanceSensor(echo=21, trigger=20)
distancias = []  # Lista para almacenar las distancias medidas
horas = []  # Lista para almacenar las horas

while True:
    
    distanciaCm = sensor.distance * 100 #Conversion a cm
    
    if distanciaCm < 10 :  
        estado = "Muy cercaaa!"
    elif distanciaCm > 10 and distanciaCm < 30 :
        estado = "Cercaaa!"
    elif distanciaCm > 30 and distanciaCm < 100 :
        estado = "Excelente!"
    elif distanciaCm > 100 and distanciaCm < 400:
        estado = "Te pasaste"
    else : estado = "Error"
    
    #Creamos documento con los datos
    documentoSensor = open("Sensor_distancia.txt", 'a')
    fechaActual = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    horaActual = datetime.now().strftime("%H:%M:%S")
    data =  f"{fechaActual} --> " \
            f" distancia: {distanciaCm} , estado: {estado}"
    documentoSensor.write(data)
    documentoSensor.close()

    # Agregar datos a las listas
    distancias.append(distanciaCm)
    horas.append(horaActual)

    # Actualizar el gráfico
    plt.plot(horas, distancias)
    plt.xlabel('Hora')
    plt.ylabel('Distancia (cm)')
    plt.title('Gráfico de Distancia vs. Hora')
    plt.grid(True)
    plt.draw()
    plt.pause(0.1)
    
    sleep(5)

