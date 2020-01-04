import RPi.GPIO as GPIO
import logging
import time

class Vibrator:

    def __init__(self, pin: int=4, warnings: bool=False, log: bool=True) -> None:
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(warnings)
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        if log:
            logging.info('vibration setup')

    def stop(self) -> None:
        GPIO.output(self.pin, GPIO.LOW)

    def run(self, duration: float=0.4, log: bool=True) -> None:
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(self.pin, GPIO.LOW)
        if log:
            logging.info('vibration on')

