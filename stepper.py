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

        GPIO.setup(self.dir_pin, GPIO.OUT)
        GPIO.setup(self.pul_pin, GPIO.OUT)
        GPIO.setup(self.ena_pin, GPIO.OUT)

        GPIO.output(self.ena_pin, GPIO.LOW)

        self.running = False
        self.stop_command = False
        self.run_count = 0

        print("...Motor ready")

    def run_stepper(self, delay, clock_wise):
        # validate parameters
        if (delay < 0.1):
            print("Delay cannot be below 0.1 milli-seconds")
            return
        
        # delay from ms to s
        delay = delay / 1000        
        
        print("Start running motor...")

        self.run_count += 1
        for i in range(5000): 
            if self.stop_command == True:
                self.stop_command = False
                print("motor stopped")
                break
            
            self.running = True

            # GPIO.output(XEnable, 0)            

            if clock_wise == True:
                GPIO.output(self.dir_pin, 1)
            else:
                GPIO.output(self.dir_pin, 0)
            
            GPIO.output(self.pul_pin, 1)
            time.sleep(delay)
            GPIO.output(self.pul_pin, 0)
            time.sleep(delay)

            # print("in run count: " + str(self.run_count))

        self.running = False
        print("Run complete")