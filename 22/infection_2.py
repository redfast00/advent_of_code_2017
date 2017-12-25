from operator import add
from collections import defaultdict
class Grid:
    def __init__(self, grid):
        self.currentloc = (0, 0)
        self.direction = (-1, 0) # up
        self.infected = defaultdict(lambda: 0)
        self.loadgrid(grid)
        self.total_infected = 0

    def loadgrid(self, grid):
        height = len(grid)
        for rowidx, row in enumerate(grid):
            width = len(row)
            for columnidx, cell in enumerate(row):
                if cell == '#':
                    self.infected[(rowidx - height//2, columnidx - width//2)] = 2
    def print_grid(self):
        for i in range(-12,13):
            for j in range(-12,13):
                if (i, j) in self.infected:
                    print('#', end='')
                else:
                    print('.', end='')
            print('')
    def step(self):
        status = self.infected[self.currentloc]
        if status == 0: # clean
            self.turnleft()
        elif status == 1: # weakened
            self.total_infected += 1
        elif status == 2: # infected
            self.turnright()
        elif status == 3:
            self.turnleft()
            self.turnleft()
        self.infected[self.currentloc] = (status+1)%4

        self.currentloc = tuple(map(add, self.direction, self.currentloc))

    def turnleft(self):
        if self.direction == (-1, 0): #up
            self.direction = (0, -1)
        elif self.direction == (0, -1):
            self.direction = (1, 0)
        elif self.direction == (1, 0):
            self.direction = (0, 1)
        elif self.direction == (0, 1):
            self.direction = (-1, 0)

    def turnright(self):
        for i in range(3):
            self.turnleft()

with open('input.txt') as infile:
    lines = [line.strip() for line in infile.readlines()]
    g = Grid(lines)
    for i in range(10000000):
        g.step()
        print(i)
    print(f'TOTAL: {g.total_infected}')
