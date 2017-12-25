class CircBuffer(object):
    def __init__(self, steps):
        self.mem = [0]
        self.steps = steps
        self.current_pos = 1
    def insert(self, value):
        self.current_pos = (self.steps + self.current_pos + 1) % (len(self.mem))
        if self.current_pos == 0:
            print("ack")
        self.mem.insert(self.current_pos, value)

steps = 377
# c = CircBuffer(steps)
# print(c.mem)
# for i in range(1, 2017):
#     c.insert(i)

cur_pos = 1
for i in range(1, 50000001):
    cur_pos = (steps + cur_pos + 1) % (i)
    if cur_pos == 0:
        print(i)
