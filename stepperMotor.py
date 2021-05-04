import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

ControlPin = [32,33,35,36,37]


for pin in ControlPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

halfseq = [ [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1],
            [1, 0, 0, 1]]

for i in range(512):
    for halfseq in range(8):
        for pin in range(4):
            GPIO.output(ControlPin[pin], halfseq[halfstep][pin])
    time.sleep(0.001)
GPIO.cleanup()