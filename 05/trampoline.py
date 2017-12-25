class FirstTrampoline:
    def __init__(self, lst):
        self.lst = lst
        self.idx = 0
    def step(self):
        if 0 <= self.idx < len(self.lst):
            old = self.idx
            self.idx += self.lst[self.idx]
            self.lst[old] += 1
            return True
        return False

class SecondTrampoline:
    def __init__(self, lst):
        self.lst = lst
        self.idx = 0
    def step(self):
        if 0 <= self.idx < len(self.lst):
            old = self.idx
            self.idx += self.lst[self.idx]
            if self.lst[old] >= 3:
                self.lst[old] -= 1
            else:
                self.lst[old] += 1
            return True
        return False

with open('input.txt') as inputfile:
    lst = [int(line) for line in inputfile.readlines()]
    first_trampoline = FirstTrampoline(lst.copy())
    steps = 0
    while first_trampoline.step():
        steps += 1
    print(steps)
    second_trampoline = SecondTrampoline(lst.copy())
    steps = 0
    while second_trampoline.step():
        steps += 1
    print(steps)
