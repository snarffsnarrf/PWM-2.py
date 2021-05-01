from classtree import (Shot)
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)    # Enable pin top
GPIO.setup(13, GPIO.OUT)    # Enable pin Bottom
GPIO.setup(16, GPIO.OUT)    # direction control t.1
GPIO.setup(18, GPIO.OUT)    # direction control t.2
GPIO.setup(29, GPIO.OUT)    # direction control b.1
GPIO.setup(31, GPIO.OUT)    # direction control b.2

t = GPIO.PWM(11, Shot.tfreq)
b = GPIO.PWM(13, Shot.bfreq)
split = 5

t.start(0)
b.start(0)

i = 0

def print_it():
    print('''

Name = {} 
Top Duty = {} | Bottom Duty = {} | 
Top Freq = {} | Bottom Freq = {} |
Top Pin  = {} | Bottom Pin = {}

            '''.format(Shot.name, Shot.tduty, Shot.bduty, Shot.tfreq, Shot.bfreq, Shot.tpin, Shot.bpin))


Shot.topspin()
print_it()
# print('''
#
# Name = {}
# Top Duty = {} | Bottom Duty = {} |
# Top Freq = {} | Bottom Freq = {} |
# Top Pin  = {} | Bottom Pin = {}
#
#         '''.format(Shot.name, Shot.tduty, Shot.bduty, Shot.tfreq, Shot.bfreq, Shot.tpin, Shot.bpin))
while i <= 5:
    print("Loop Start")
    print(i + 1)
    Shot.topspin()
    t.ChangeFrequency(Shot.tfreq)
    b.ChangeFrequency(Shot.bfreq)
    t.ChangeDutyCycle(Shot.tduty)
    b.ChangeDutyCycle(Shot.bduty)
    print_it()
    time.sleep(split)
    Shot.backspin()
    t.ChangeFrequency(Shot.tfreq)
    b.ChangeFrequency(Shot.bfreq)
    t.ChangeDutyCycle(Shot.tduty)
    b.ChangeDutyCycle(Shot.bduty)
    print_it()
    time.sleep(split)
    i = i + 1
GPIO.cleanup()


# Shot = Shot(1, 1, 0, 0, 0, 0)
