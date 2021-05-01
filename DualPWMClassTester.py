import RPi.GPIO as GPIO
import time
from shotLibraryClass import Shot
from shotLibraryClass import shottype



mainfreq = 500
Shot.tpin = 11
Shot.bpin = 13
Shot.tfreq = mainfreq
Shot.bfreq = mainfreq

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Shot.tpin, GPIO.OUT)    # Enable pin top
GPIO.setup(Shot.bpin, GPIO.OUT)    # Enable pin Bottom
GPIO.setup(16, GPIO.OUT)    # direction control t.1
GPIO.setup(18, GPIO.OUT)    # direction control t.2
GPIO.setup(29, GPIO.OUT)    # direction control b.1
GPIO.setup(31, GPIO.OUT)    # direction control b.2


t = GPIO.PWM(Shot.tpin, Shot.tfreq)
b = GPIO.PWM(Shot.bpin, Shot.bfreq)

awf = 0
low = 30
med = 50
high = 100

i = 1
GPIO.output(16, False)
GPIO.output(18, True)
GPIO.output(29, False)
GPIO.output(31, True)


while i <= 10:
    print("""
LOOP START
__________
          """)
    print(i)
    time.sleep(1)
    t.start(0)
    b.start(0)
    print("Start")
    time.sleep(2)
    t.ChangeDutyCycle(low)
    b.ChangeDutyCycle(low)
    print("Low")
    time.sleep(5)
    t.ChangeDutyCycle(med)
    b.ChangeDutyCycle(med)
    print("Med")
    time.sleep(5)
    t.ChangeDutyCycle(high)
    b.ChangeDutyCycle(high)
    print("High")
    time.sleep(5)
    t.ChangeDutyCycle(med)
    b.ChangeDutyCycle(med)
    print("Med")
    time.sleep(5)
    t.ChangeDutyCycle(high)
    b.ChangeDutyCycle(high)
    print("high")
    time.sleep(5)
    t.ChangeDutyCycle(low)
    b.ChangeDutyCycle(low)
    print("Low")
    time.sleep(5)
    i = (i + 1)
t.stop()
b.stop()
GPIO.cleanup()
