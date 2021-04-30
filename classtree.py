# import RPi.GPIO as GPIO



class Shot:
    def __init__(self, tfreq, bfreq, tpin, bpin, tduty, bduty):
        self.tfreq = tfreq
        self.bfreq = bfreq
        self.tpin = tpin
        self.bpin = bpin
        self.tduty = tduty
        self.bduty = bduty

    def shotout(self):
        return '{} {} {} {} {} {}'.format(self.tfreq, self.bfreq, self.tpin, self.bpin, self.tduty, self.bduty)

    def shotout2(self):
        pass

def shottype():
    Shot(50, 50, 11, 13, 50, 40)
    Shot(80, 80, 11, 13, 100, 100)




print(Shot.shotout())
shottype()
print(Shot.shotout())



