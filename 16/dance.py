import string
class DanceRoom(object):
    def __init__(self):
        self.positions = [string.ascii_lowercase[i] for i in range(16)]
        print(self.positions)
    def spin(self, size):
        self.positions = self.positions[-size:] + self.positions[:-size]
    def exchange(self, idx_a, idx_b):
        # Warning: 0-indexed
        a = self.positions[idx_a]
        b = self.positions[idx_b]
        self.positions[idx_a] = b
        self.positions[idx_b] = a
    def partner(self, a, b):
        idx_a = self.positions.index(a)
        idx_b = self.positions.index(b)
        self.positions[idx_a] = b
        self.positions[idx_b] = a

d = DanceRoom()
found = {}
i = 0
current = ''.join(d.positions)
with open('input.txt') as infile:
    moves = infile.read().strip().split(',')

while current not in found:
    found[current] = i
    for move in moves:
        operation = move[0]
        if operation == 's':
            d.spin(int(move[1:]))
        elif operation == 'x':
            args = move[1:].split('/')
            d.exchange(int(args[0]), int(args[1]))
        elif operation == 'p':
            args = move[1:].split('/')
            d.partner(args[0], args[1])
    current = ''.join(d.positions)
    i += 1
print(found[current])
idx = 1000000000 % (i - found[current])
for k, v in found.items():
    if v == idx:
        print(k)
