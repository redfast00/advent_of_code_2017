class Generator(object):
    def __init__(self, number, factor, divider):
        self.number = number
        self.factor = factor
        self.divider = divider
    def next(self):
        self.number = (self.number * self.factor) % 2147483647
        while self.number % self.divider != 0:
            self.number = (self.number * self.factor) % 2147483647
        return self.number

class Judge(object):
    def __init__(self):
        self.A = Generator(512, 16807, 4)
        self.B = Generator(191, 48271, 8)
    def do_steps(self, steps):
        ctr = 0
        for i in range(steps):
            if (self.A.next() & 0xFFFF) == (self.B.next() & 0xFFFF):
                ctr += 1
                print(ctr, i)
        return ctr

j = Judge()
print(j.do_steps(5 * 1000 * 1000))
