from classtree import (Shot)
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(Shot.tpin, GPIO.OUT)    # Enable pin top
GPIO.setup(Shot.bpin, GPIO.OUT)    # Enable pin Bottom
GPIO.setup(16, GPIO.OUT)    # direction control t.1
GPIO.setup(18, GPIO.OUT)    # direction control t.2
GPIO.setup(29, GPIO.OUT)    # direction control b.1
GPIO.setup(31, GPIO.OUT)    # direction control b.2

t = GPIO.PWM(Shot.tpin, Shot.tfreq)
b = GPIO.PWM(Shot.bpin, Shot.bfreq)
Shot = Shot(0, 0, 0, 0, 0, 0)


Shot.topspin()
while True:
    t.ChangeDutyCycle(Shot.tduty())
    b.ChangeDutyCycle(Shot.bduty())
    print('{} - {}'.format(Shot.tduty, Shot.bduty))
    break
time.sleep(5)
Shot.backspin()
while True:
    t.ChangeDutyCycle(Shot.bduty())
    b.ChangeDutyCycle(Shot.bduty())
    print('{} - {}'.format(Shot.tduty, Shot.bduty))
    break

