Hfreq = 100
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

    def startup(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.tpin = toppin
        self.bpin = botpin
        self.tduty = 40
        self.bduty = 40
        self.name = "Starting Motors"

    def topspin(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.tpin = toppin
        self.bpin = botpin
        self.tduty = 70
        self.bduty = 50
        self.name = "Topspin"

    def backspin(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.tpin = toppin
        self.bpin = botpin
        self.tduty = 50
        self.bduty = 70
        self.name = "Backspin"

    def deeptopspin(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.tpin = toppin
        self.bpin = botpin
        self.tduty = 100
        self.bduty = 70
        self.name = "DeepTopspin"

    def deepbackspin(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.tpin = toppin
        self.bpin = botpin
        self.tduty = 70
        self.bduty = 100
        self.name = "Deep Backspin"

    def dropshot(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.tpin = toppin
        self.bpin = botpin
        self.tduty = 30
        self.bduty = 35
        self.name = "Dropshot"


# def Shottype(self):
#     self.topspin = Shot.topspin()


Shot = Shot(100, 100, 0, 0, 0, 0, 0)

def output():
    return 'Top Freq={} | Bot Freq={} | Top Pin={} | Bot Pin={} | TDuty {} | Bduty {}'\
        .format(Shot.tfreq, Shot.bfreq, Shot.tpin, Shot.bpin, Shot.tduty, Shot.bduty)
