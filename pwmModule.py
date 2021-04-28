import RPi.GPIO as GPIO
import time

class Freq:
    def __init__(self, tfreq, bfreq):
        self.tfreq = tfreq
        self.bfreq = bfreq


def pwm(pin, freq):
    GPIO.PWM(pin, freq)

pwm(11, bfreq)

