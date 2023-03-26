class Coin:
    def __init__(self):
        self.side_up = 'Орёл'
    def toss(self):
        up = random.randint(0, 7)
        if up >= 0 and up < 3:
            self.side_up = 'Орёл'
        elif up >= 3 and up < 7:
            self.side_up = 'Решка'
        else:
            self.side_up = 'Боковая сторона'
    def  get_side_up(self):
        return self.side_up
