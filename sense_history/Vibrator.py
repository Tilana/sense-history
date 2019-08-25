import RPi.GPIO as GPIO
import time

class Vibrator:

    def __init__(self, pin=4, warnings=False):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(warnings)
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

    def stop(self):
        GPIO.output(self.pin, GPIO.LOW)

    def run(self, duration=1):
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(self.pin, GPIO.LOW)

