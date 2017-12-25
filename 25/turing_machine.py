from collections import defaultdict
from collections import Counter

class TuringMachine():
    def __init__(self):
        self.state = 'A'
        self.tapelocation = 0
        self.tape = defaultdict(lambda: 0)
        self.steps = 0
        self.perform_diag = 12459852

    def step(self):
        getattr(self, self.state)()

    def get_current_value(self):
        return self.tape[self.tapelocation]

    def write(self, value):
        self.tape[self.tapelocation] = value

    def left(self):
        self.tapelocation -= 1

    def right(self):
        self.tapelocation += 1

    def count(self):
        c = Counter(self.tape.values())
        return c[1]
    def step_and_checksum(self):
        for i in range(self.perform_diag):
            self.step()
        return self.count()

    def A(self):
        if self.get_current_value() == 0:
            self.write(1)
            self.right()
            self.state = 'B'
        else:
            # self.write(1)
            self.left()
            self.state = 'E'
    def B(self):
        if self.get_current_value() == 0:
            self.write(1)
            self.right()
            self.state = 'C'
        else:
            # self.write(1)
            self.right()
            self.state = 'F'
    def C(self):
        if self.get_current_value() == 0:
            self.write(1)
            self.left()
            self.state = 'D'
        else:
            self.write(0)
            self.right()
            self.state = 'B'
    def D(self):
        if self.get_current_value() == 0:
            self.write(1)
            self.right()
            self.state = 'E'
        else:
            self.write(0)
            self.left()
            self.state = 'C'
    def E(self):
        if self.get_current_value() == 0:
            self.write(1)
            self.left()
            self.state = 'A'
        else:
            self.write(0)
            self.right()
            self.state = 'D'
    def F(self):
        if self.get_current_value() == 0:
            self.write(1)
            self.right()
            self.state = 'A'
        else:
            # self.write(1)
            self.right()
            self.state = 'C'

t = TuringMachine()
print(t.step_and_checksum())
