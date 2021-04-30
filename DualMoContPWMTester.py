import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)    # Enable pin top
GPIO.setup(13, GPIO.OUT)    # Enable pin Bottom
GPIO.setup(16, GPIO.OUT)    # direction control t.1
GPIO.setup(18, GPIO.OUT)    # direction control t.2
GPIO.setup(29, GPIO.OUT)    # direction control b.1
GPIO.setup(31, GPIO.OUT)    # direction control b.2


t = GPIO.PWM(11, 500)
b = GPIO.PWM(13, 500)

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
