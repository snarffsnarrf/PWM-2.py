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



Shot.topspin()
while True:
    t.ChangeDutyCycle(Shot.tduty)
    b.ChangeDutyCycle(Shot.bduty)
    print('Top Duty = {} | Bottom Duty = {} | Name = {} |'.format(Shot.tduty, Shot.bduty, Shot.name))
    break
time.sleep(5)
Shot.backspin()
while True:
    t.ChangeDutyCycle(Shot.bduty)
    b.ChangeDutyCycle(Shot.bduty)
    print('Top Duty = {} | Bottom Duty = {} | Name = {} |'.format(Shot.tduty, Shot.bduty, Shot.name))
    break
GPIO.cleanup()


# Shot = Shot(1, 1, 0, 0, 0, 0)
