import RPi.GPIO as GPIO
import time




class Freq:
    def __init__(self, tfreq, bfreq):
        self.tfreq = tfreq
        self.bfreq = bfreq


class Pin:
    def __init__(self, pin):
        self.pin = pin

class DutyCycle:
    def __init__(self, tduty, bduty):
        self.tduty = tduty
        self.bduty = bduty

class Motor:
    def __init__(self, t, b):
        self.t = GPIO.PWM(11, Freq.tfreq)
        self.b = GPIO.PWM(13, Freq.bfreq)

def pwm(pin, freq):
    GPIO.PWM(pin, freq)

def duty(tfreq, bfreq):
    ChangeDutyCycle(tfreq)
    ChangeDutyCycle(bfreq)




pwm(Pin.pin, Freq.tfreq)

Freq.tfreq = 500
Freq.bfreq = 500
Pin.pin = 11