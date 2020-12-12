# pulper 

import RPi.GPIO as GPIO
import time

class Motor(object):
    def __init__(self):
        print("Initializing Motor...")
        # ENA - GPIO 16 - Enable Offline Turning
        # DIR - GPIO 20
        # PUL = GPIO 26

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        self.dir_pin = 20
        self.pul_pin = 26
        self.ena_pin = 16

        self.delay = 0.0005

        GPIO.setup(self.dir_pin, GPIO.OUT)
        GPIO.setup(self.pul_pin, GPIO.OUT)
        GPIO.setup(self.ena_pin, GPIO.OUT)

        GPIO.output(self.ena_pin, GPIO.LOW)

        print("...Motor ready")

    def pulse_x_ccw(self):
        print("Running motor...")
        for i in range(5000): 
            # GPIO.output(XEnable, 0)

            GPIO.output(self.dir_pin, 0)
            
            GPIO.output(self.pul_pin, 1)
            time.sleep(self.delay)
            GPIO.output(self.pul_pin, 0)
            time.sleep(self.delay)

            # print ("Moving X CCW \n")


# pulse_x_ccw()