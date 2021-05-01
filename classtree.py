# import RPi.GPIO as GPIO
import time

Hfreq = 100
Lfreq = 50
Tpin = 11
Bpin = 13



class Shot:

    def __init__(self, tfreq, bfreq, tpin, bpin, tduty, bduty):
        self.tfreq = tfreq
        self.bfreq = bfreq
        self.tpin = tpin
        self.bpin = bpin
        self.tduty = tduty
        self.bduty = bduty

    def topspin(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.tpin = Tpin
        self.bpin = Bpin
        self.tduty = 100
        self.bduty = 80

    def backspin(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.tpin = Tpin
        self.bpin = Bpin
        self.tduty = 80
        self.bduty = 100


def Shottype(self):
    self.topspin = Shot.topspin()





Shot = Shot(0, 0, 0, 0, 0, 0)

def output():
    return 'Top Freq={} | Bot Freq={} | Top Pin={} | Bot Pin={} | TDuty {} | Bduty {}'\
        .format(Shot.tfreq, Shot.bfreq, Shot.tpin, Shot.bpin, Shot.tduty, Shot.bduty)

