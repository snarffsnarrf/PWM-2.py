
toppin = 11
botpin = 13


class Shot:

    def __init__(self, tfreq, bfreq, toppin, botpin, tduty, bduty, name):
        self.tfreq = tfreq
        self.bfreq = bfreq
        self.tpin = toppin
        self.bpin = botpin
        self.tduty = tduty
        self.bduty = bduty
        self.name = name

    def topspin(self):
        self.tfreq = 150
        self.bfreq = 150
        self.tpin = toppin
        self.bpin = botpin
        self.tduty = 100
        self.bduty = 50
        self.name = "Topspin"

    def backspin(self):
        self.tfreq = 200
        self.bfreq = 200
        self.tpin = toppin
        self.bpin = botpin
        self.tduty = 80
        self.bduty = 100
        self.name = "Backspin"


# def Shottype(self):
#     self.topspin = Shot.topspin()


Shot = Shot(100, 100, 0, 0, 0, 0, 0)

def output():
    return 'Top Freq={} | Bot Freq={} | Top Pin={} | Bot Pin={} | TDuty {} | Bduty {}'\
        .format(Shot.tfreq, Shot.bfreq, Shot.tpin, Shot.bpin, Shot.tduty, Shot.bduty)
