import RPi.GPIO as GPIO
import time

SENSOR_PIN = 5

def esperar_cero(logger):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    logger.info("Esperando posición cero...")
    while GPIO.input(SENSOR_PIN) == GPIO.LOW:
        time.sleep(0.1)
    logger.info("¡Posición cero detectada!")
    GPIO.cleanup()