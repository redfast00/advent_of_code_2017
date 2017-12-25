class TwoDimensionalDriver:
    def __init__(self, default=0):
        self.mem = {}
        self.default = 0
    def get(self, x, y):
        return self.mem.get((x,y), self.default)
    def set(self, x, y, value):
        self.mem[(x,y)] = value



def surrounding_sum(twodim, x, y):
    total = 0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            total += twodim.get(x+i, y+j)
    print(x, y,total)
    return total

def get_level(cell):
    i = 0
    while cell > (2*i+1)**2:
        i += 1
    return i

def find_max(tofind):
    twodim = TwoDimensionalDriver()
    twodim.set(0, 0, 1)
    level = 0
    x = 0
    y = 0
    while True:
        while (x,y) != (level, level):
            sum = surrounding_sum(twodim, x, y)
            twodim.set(x, y, sum)
            if sum > tofind:
                return sum
            y += 1
        while (x,y) != (-level, level):
            sum = surrounding_sum(twodim, x, y)
            twodim.set(x, y, sum)
            if sum > tofind:
                return sum
            x -= 1
        while (x,y) != (-level, -level):
            sum = surrounding_sum(twodim, x, y)
            twodim.set(x, y, sum)
            if sum > tofind:
                return sum
            y -= 1
        while (x,y) != (level, -level):
            sum = surrounding_sum(twodim, x, y)
            twodim.set(x, y, sum)
            if sum > tofind:
                return sum
            x += 1
        sum = surrounding_sum(twodim, x, y)
        twodim.set(x, y, sum)
        if sum > tofind:
            return sum
        print("at end of level")
        x += 1
        level += 1

tofind = int(input())
print(find_max(tofind))
