Hfreq = 200
top_pin = 11
bot_pin = 13

hhspd = 100
hspd = 95
mspd = 85
lspd =75


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
        self.tpin = top_pin
        self.bpin = bot_pin
        self.tduty = lspd
        self.bduty = lspd
        self.name = "Starting Motors"

    def t_spin(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.tpin = top_pin
        self.bpin = bot_pin
        self.tduty = hspd
        self.bduty = mspd
        self.name = "Topspin"

    def b_spin(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.tpin = top_pin
        self.bpin = bot_pin
        self.tduty = mspd
        self.bduty = hspd
        self.name = "Backspin"

    def d_t_spin(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.tpin = top_pin
        self.bpin = bot_pin
        self.tduty = hhspd
        self.bduty = hspd
        self.name = "DeepTopspin"

    def d_b_spin(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.tpin = top_pin
        self.bpin = bot_pin
        self.tduty = hspd
        self.bduty = hhspd
        self.name = "Deep Backspin"

    def d_shot(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.tpin = top_pin
        self.bpin = bot_pin
        self.tduty = mspd
        self.bduty = mspd
        self.name = "Dropshot"

    def wideopen(self):
        self.tfreq = Hfreq
        self.bfreq = Hfreq
        self.tpin = top_pin
        self.bpin = bot_pin
        self.tduty = hhspd
        self.bduty = hhspd
        self.name = "Wide Open"

# def Shottype(self):
#     self.topspin = Shot.topspin()


Shot = Shot(100, 100, 0, 0, 0, 0, 0)

def output():
    return 'Top Freq={} | Bot Freq={} | Top Pin={} | Bot Pin={} | TDuty {} | Bduty {}'\
        .format(Shot.tfreq, Shot.bfreq, Shot.tpin, Shot.bpin, Shot.tduty, Shot.bduty)
