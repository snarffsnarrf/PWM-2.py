from classtree import (Shot)
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)    # Enable pin Top
GPIO.setup(13, GPIO.OUT)    # Enable pin Bottom
GPIO.setup(16, GPIO.OUT)    # direction control t.1
GPIO.setup(18, GPIO.OUT)    # direction control t.2
GPIO.setup(29, GPIO.OUT)    # direction control b.1
GPIO.setup(31, GPIO.OUT)    # direction control b.2

t = GPIO.PWM(11, Shot.tfreq)    # GPIO.PWM instance start
b = GPIO.PWM(13, Shot.bfreq)    # GPIO.PWM instance start
split = 5                       # Time Between shots


def print_it():
    print('''

Name = {} 
Top Duty = {} | Bottom Duty = {} | 
Top Freq = {} | Bottom Freq = {} |
Top Pin  = {} | Bottom Pin = {}

            '''.format(Shot.name, Shot.tduty, Shot.bduty, Shot.tfreq, Shot.bfreq, Shot.tpin, Shot.bpin))


def shot_instance():
    t.ChangeFrequency(Shot.tfreq)
    b.ChangeFrequency(Shot.bfreq)
    t.ChangeDutyCycle(Shot.tduty)
    b.ChangeDutyCycle(Shot.bduty)


t.start(0)                                  # Begin PWM
b.start(0)                                  # Begin PWM
i = 0                                       # Instance for timing
Shot.topspin()
print_it()
while i <= 2:                               # Where number is the amount of rounds
    print("Loop Start")
    print(i + 1)
    Shot.topspin()
    shot_instance()
    print_it()
    time.sleep(split)
    Shot.backspin()
    shot_instance()
    print_it()
    time.sleep(split)
    i = i + 1
GPIO.cleanup()


# Shot = Shot(1, 1, 0, 0, 0, 0)
