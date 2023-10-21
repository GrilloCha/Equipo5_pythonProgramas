import adafruit_dht
import matplotlib.pyplot as plt
import board

#Configuramos pin
sensor = adafruit_dht.DHT11(board.D7)

#Listas para el grafico
temperaturaGrafico = []
humedadGrafico = []

while True:
    temperatura_C = sensor.temperature
    humedad = sensor.humidity
    
     # Agregar datos a las listas
    temperaturaGrafico.append(temperatura_C)
    humedadGrafico.append(humedad)
    
    #Imprimimos datos
    print(f"Temperatura: {temperatura_C}  Humedad: {humedad}")

    # Actualizar el gráfico
    plt.plot(temperaturaGrafico, color='red', label='Temperatura')
    plt.plot(humedadGrafico, color='blue', label='Humedad')
    plt.xlabel('Temperatura (C)')
    plt.ylabel('Humedad')
    plt.title('Temperatura vs Humedad')
    plt.grid(True)
    plt.draw()
    plt.pause(0.1)