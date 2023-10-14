from gpiozero import LED
import time
    
led = LED(17)

try:
    tiempo = float(input("Tiempo en segundos de encendido del LED: "))

    led.on()   
    time.sleep(tiempo)
    led.off()
except KeyboardInterrupt:
    pass
finally:
    led.close()
