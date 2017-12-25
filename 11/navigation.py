class Navigation(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.furthest = 0
    def addmove(self, navigationstring):
        for letter in navigationstring:
            if letter == 'n':
                self.y += 1
            elif letter == 's':
                self.y -=1
            elif letter == 'e':
                self.x += 1
            elif letter == 'w':
                self.x -= 1
            distance = max(abs(navigator.x), abs(navigator.y))
            self.furthest = max(distance, self.furthest)

with open('input.txt') as logfile:
    line = logfile.read().strip()
    moves = line.split(',')
    navigator = Navigation()
    for move in moves:
        navigator.addmove(move)
    print(max(abs(navigator.x), abs(navigator.y)))
    print(navigator.furthest)
