from collections import defaultdict

class CPU(object):
    def __init__(self, instructions):
        self.instructions = instructions
        self.ip = 0
        self.played_sound = 0
        self.registers = defaultdict(lambda: 0)
    def step(self):
        if 0 <= self.ip < len(self.instructions):
            instruction = self.instructions[self.ip]
        else:
            print("DONE")
            return False
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
            self.rcv(instruction)
        elif name == 'jgz':
            self.jgz(instruction)
        else:
            print("unknown instruction")
        self.ip += 1
        return True

    def get_value(self, name):
        try:
            value = int(name)
        except:
            value = self.registers[name]
        return value
    def snd(self, i):
        self.played_sound = self.get_value(i[1])
    def set(self, i):
        self.registers[i[1]] = self.get_value(i[2])
    def mul(self, i):
        self.registers[i[1]] *= self.get_value(i[2])
    def mod(self, i):
        self.registers[i[1]] = self.get_value(i[1]) % self.get_value(i[2])
    def add(self, i):
        self.registers[i[1]] += self.get_value(i[2])
    def rcv(self, i):
        if self.played_sound != 0:
            print(self.played_sound)
            self.registers[i[1]] = self.played_sound
    def jgz(self, i):
        if self.get_value(i[1]) > 0:
            self.ip += self.get_value(i[2]) - 1

with open('input.txt') as ifile:
    instructions = [ins.strip().split(' ') for ins in ifile.readlines()]
    c = CPU(instructions)
    while c.step():
        pass
