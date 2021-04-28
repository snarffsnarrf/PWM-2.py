from pwmModule import (Freq, Pin, pwm)  # Maybe I'm doing this right?

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)    # direction control t.1
GPIO.setup(18, GPIO.OUT)    # direction control t.2
GPIO.setup(29, GPIO.OUT)    # direction control b.1
GPIO.setup(31, GPIO.OUT)    # direction control b.2

Freq.tfreq = 100
Freq.bfreq = 100


while True:
    pwm(13, Freq.tfreq)
    pwm(11, Freq.bfreq)


Pin.pin = 11