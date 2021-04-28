from pwmModule import (Freq, Pin, pwm)  # Maybe I'm doing this right?

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)    # direction control t.1
GPIO.setup(18, GPIO.OUT)    # direction control t.2
GPIO.setup(29, GPIO.OUT)    # direction control b.1
GPIO.setup(31, GPIO.OUT)    # direction control b.2



pwm(Pin.pin, Freq.tfreq)
pwm(Pin.pin, Freq.bfreq)

Freq.tfreq = 5
Pin.pin = 11