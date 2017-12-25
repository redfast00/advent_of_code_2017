from collections import defaultdict, deque

class CPU(object):
    def __init__(self, instructions, _id):
        self.instructions = instructions
        self.ip = 0
        self.registers = defaultdict(lambda: 0)
        self.registers['p'] = _id
        self._id = _id
        self.outqueue = deque()
        self.inqueue = [] #TODO
        self.sent = 0
    def step(self):
        if 0 <= self.ip < len(self.instructions):
            instruction = self.instructions[self.ip]
        else:
            print("DONE")
            return False, False
        name = instruction[0]
        if name == 'snd':
            self.snd(instruction)
        elif name == 'set':
            self.set(instruction)
        elif name == 'mul':
            self.mul(instruction)
        elif name == 'add':
            self.add(instruction)
        elif name == 'mod':
            self.mod(instruction)
        elif name == 'rcv':
            if not self.rcv(instruction):
                # We need to switch cpu sides
                return True, True
        elif name == 'jgz':
            self.jgz(instruction)
        else:
            print("unknown instruction")
        self.ip += 1
        return True, False

    def get_value(self, name):
        try:
            value = int(name)
        except:
            value = self.registers[name]
        return value
    def snd(self, i):
        self.outqueue.append(self.get_value(i[1]))
        if self._id == 1:
            self.sent += 1
            print(f's = {self.sent}')
            pass
    def set(self, i):
        self.registers[i[1]] = self.get_value(i[2])
    def mul(self, i):
        self.registers[i[1]] *= self.get_value(i[2])
    def mod(self, i):
        self.registers[i[1]] = self.get_value(i[1]) % self.get_value(i[2])
    def add(self, i):
        self.registers[i[1]] += self.get_value(i[2])
    def rcv(self, i):
        if len(self.inqueue) == 0:
            return False
        else:
            self.registers[i[1]] = self.inqueue.popleft()
            return True
    def jgz(self, i):
        if self.get_value(i[1]) > 0:
            self.ip += self.get_value(i[2]) - 1

    def continue_rcv(self):
        i = self.instructions[self.ip]
        if len(self.inqueue) == 0:
            return False
        else:
            self.registers[i[1]] = self.inqueue.popleft()
            self.ip += 1
            return True

def do_things():
    with open('input.txt') as ifile:
        instructions = [ins.strip().split(' ') for ins in ifile.readlines()]
        c0 = CPU(instructions, 0)
        c1 = CPU(instructions, 1)
        c1.inqueue = c0.outqueue
        c0.inqueue = c1.outqueue
        while True:
            running0, waiting0 = c0.step()
            if waiting0:
                while not(c0.continue_rcv()):
                    running1, waiting1 = c1.step()
                    if waiting1 or not running1:
                        print('deadlock')
                        return True
            running1, waiting1 = c1.step()
            if waiting1:
                while not(c1.continue_rcv()):
                    running0, waiting0 = c0.step()
                    if waiting0 or not running0:
                        print('deadlock')
                        return True
            if not (running0 and running1):
                print("stopped")
                print(c0.ip)
                print(c1.ip)
                return True

do_things()
