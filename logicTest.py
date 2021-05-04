from shotLibraryClass import (Shot)
import time
import random
import RPi.GPIO as GPIO
from random import choice


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)    # Enable pin Top
GPIO.setup(13, GPIO.OUT)    # Enable pin Bottom
GPIO.setup(16, GPIO.OUT)    # direction control t.1
GPIO.setup(18, GPIO.OUT)    # direction control t.2
GPIO.setup(29, GPIO.OUT)    # direction control b.1
GPIO.setup(31, GPIO.OUT)    # direction control b.2

t = GPIO.PWM(11, Shot.tfreq)    # GPIO.PWM instance start
b = GPIO.PWM(13, Shot.bfreq)    # GPIO.PWM instance start


def split():
    return random.randint(3, 10)                      # Random time Between shots


def print_it():
    print('''

Name = {} 
Top Duty = {} | Top Freq = {} | Top Pin = {} 
Bot Duty = {} | Bot Freq = {} | Bot Pin = {}
 

            '''.format(Shot.name, Shot.tduty, Shot.tfreq, Shot.tpin, Shot.bduty,  Shot.bfreq,  Shot.bpin))


def shot_instance():
    t.ChangeFrequency(Shot.tfreq)
    b.ChangeFrequency(Shot.bfreq)
    t.ChangeDutyCycle(Shot.tduty)
    b.ChangeDutyCycle(Shot.bduty)


Shotlist = [Shot.t_spin, Shot.d_t_spin, Shot.b_spin, Shot.d_b_spin, Shot.d_shot, Shot.wideopen]


t.start(0)                                  # Begin PWM
b.start(0)                                  # Begin PWM
i = 0                                       # Instance for timing
ShotNumber = i + 1
Shot.startup()
shot_instance()
print_it()
time.sleep(split())
while i <= 100:                               # Where number is the amount of rounds
    print("Shot Number: ")
    print(i + 1)
    choice(Shotlist)()
    split()
    shot_instance()
    print_it()
    time.sleep(split())
    i = i + 1
GPIO.cleanup()


# Shot = Shot(1, 1, 0, 0, 0, 0)
