from pwmModule import (Freq, Pin, pwm, DutyCycle, duty, Motor)  # Maybe I'm doing this right?
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)    # direction control t.1
GPIO.setup(18, GPIO.OUT)    # direction control t.2
GPIO.setup(29, GPIO.OUT)    # direction control b.1
GPIO.setup(31, GPIO.OUT)    # direction control b.2

Freq.tfreq = 0
Freq.bfreq = 0
DutyCycle.tduty = 0
DutyCycle.bduty = 0




while True:
    t.start(Freq.tfreq)
    pwm(13, Freq.tfreq)
    pwm(11, Freq.bfreq)




