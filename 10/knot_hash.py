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

with open("input") as taskfile:
    task = taskfile.read().strip()
    r = Rope()
    for amount in task.split(','):
        r.tie(int(amount))
    print(r.memory[0:2])

with open("input") as taskfile:
    task = [ord(char) for char in taskfile.read().strip()] + [17, 31, 73, 47, 23]
    r = Rope()
    for i in range(64):
        for amount in task:
            r.tie(amount)
    result = []
    for i in range(16):
        result.append(densehash(r.memory[16*i:16*(i+1)]))
    hexed = ["{0:0{1}x}".format(number,2) for number in result]
    print(''.join(hexed))
