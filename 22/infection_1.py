from operator import add
class Grid:
    def __init__(self, grid):
        self.currentloc = (0, 0)
        self.direction = (-1, 0) # up
        self.infected = {}
        self.loadgrid(grid)
        self.total_infected = 0

    def loadgrid(self, grid):
        height = len(grid)
        for rowidx, row in enumerate(grid):
            width = len(row)
            for columnidx, cell in enumerate(row):
                if cell == '#':
                    print((rowidx - height//2, columnidx - 2//width))
                    self.infected[(rowidx - height//2, columnidx - width//2)] = True
    def print_grid(self):
        for i in range(-12,13):
            for j in range(-12,13):
                if (i, j) in self.infected:
                    print('#', end='')
                else:
                    print('.', end='')
            print('')
    def step(self):
        if self.currentloc in self.infected:
            self.turnright()
            del self.infected[self.currentloc]
        else:
            self.infected[self.currentloc] = True
            self.turnleft()
            self.total_infected += 1
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
    for i in range(10000):
        g.step()
    print(g.total_infected)
