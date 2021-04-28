import RPi.GPIO as GPIO
import time


class Freq:
    def __init__(self, tfreq, bfreq):
        self.tfreq = tfreq
        self.bfreq = bfreq


class Pin:
    def __init__(self, pin):
        self.pin = pin


def pwm(pin, freq):
    GPIO.PWM(pin, freq)




pwm(Pin.pin, Freq.tfreq)

Freq.tfreq = 5
Pin.pin = 11