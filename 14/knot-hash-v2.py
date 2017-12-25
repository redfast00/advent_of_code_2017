import operator
from functools import reduce

class Rope(object):
    def __init__(self):
        self.memory = list(range(256))
        self.skipping_size = 0
        self.current_position = 0

    def get(self, idx):
        return self.memory[idx % len(self.memory)]

    def set(self, idx, value):
        self.memory[idx % len(self.memory)] = value

    def tie(self, amount):
        newmem = [self.get(self.current_position+i) for i in range(amount)]
        for idx, i in enumerate(reversed(newmem)):
            self.set(idx + self.current_position, i)
        self.current_position += self.skipping_size + amount
        self.skipping_size += 1

def densehash(lst):
    return reduce(operator.xor, lst)


def knothash(chars):
    task = [ord(char) for char in chars] + [17, 31, 73, 47, 23]
    r = Rope()
    for i in range(64):
        for amount in task:
            r.tie(amount)
    result = []
    for i in range(16):
        result.append(densehash(r.memory[16*i:16*(i+1)]))
    hexed = ["{0:0{1}x}".format(number,2) for number in result]
    return ''.join(hexed)

def mark_region(table, x, y):
    queue = []
    queue.append((x,y))
    while len(queue) != 0:
        x, y = queue.pop(0)
        table[x][y] = '0'
        for dx, dy in [(1,0), (0,1), (-1,0),(0,-1)]:
            if (0 <= x+dx < 128 and 0 <= y+dy < 128):
                here = table[x+dx][y+dy]
                if here == '1':
                    queue.append((x+dx,y+dy))
                    table[x+dx][y+dy] = '0'


# def remove_group(table, x, y):
#     if not (0 <= x < 128 and 0 <= y < 128):
#         return
#     if table[x][y] == '0':
#         return
#     table[x][y] = '0'
#     remove_group(table, x+1, y)
#     remove_group(table, x, y+1)
#     remove_group(table, x-1, y)
#     remove_group(table, x, y-1)

def count_regions(table):
    ctr = 0
    for i in range(128):
        for j in range(128):
            if table[i][j] == '1':
                # remove_group(table, i, j)
                mark_region(table, i, j)
                ctr += 1
    return ctr

ctr = 0
key = 'jzgqcdpd'
table = []
for i in range(128):
    t = knothash(f'{key}-{i}')
    number = int(t, 16)
    binary = format(number, '0128b')
    table.append([c for c in binary])
    print(binary)
    ctr += binary.count('1')
print(ctr)
print(count_regions(table))
