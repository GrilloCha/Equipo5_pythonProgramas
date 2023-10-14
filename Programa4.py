from gpiozero import LED
import time

ledRojo = LED(17)
ledAmarillo = LED(2)
ledVerde = LED(3)

while True:
    ledVerde.on()
    time.sleep(3)
    ledVerde.off()
    
    ledAmarillo.on()
    time.sleep(3)
    ledAmarillo.off()
    
    ledRojo.on()
    time.sleep(3)
    ledRojo.off()