import RPi.GPIO as GPIO
import logging
import time

class Vibrator:

    def __init__(self, pin=4, warnings=False, log=True):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(warnings)
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        if log:
            logging.info('vibration setup')

    def stop(self):
        GPIO.output(self.pin, GPIO.LOW)

    def run(self, duration=0.4, log=True):
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(self.pin, GPIO.LOW)
        if log:
            logging.info('vibration on')

