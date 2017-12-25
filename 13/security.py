def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

class Laser(object):
    def __repr__(self):
        return f'Laser({self.currentloc})'
    def __init__(self, depth, _range):
        self.range = _range
        self.depth = depth
        self.currentloc = 1
        self.direction = -1
    def step(self):
        if self.currentloc == 1 or self.currentloc == self.range:
            self.direction *= -1
        self.currentloc += self.direction
    def is_active(self):
        return self.currentloc == 1
    def is_safe_after(self, steps):
        return (steps + self.depth) % (2*(self.range - 1)) != 0
    def cost(self):
        return self.range * self.depth

class Firewall(object):
    def __init__(self):
        self.lasers = {}
        self.packetloc = -1
        self.packetcost = 0
        self.max_delay = 1
    def add_laser(self, laser):
        self.lasers[laser.depth] = laser
        self.max_delay = lcm(self.max_delay, laser.range)
    def steplasers(self):
        for laser in self.lasers.values():
            laser.step()
    def skiplasers(self, steps):
        for laser in self.lasers.values():
            laser.skip(steps)
    def step(self):
        self.packetloc += 1
        if self.packetloc in self.lasers and self.lasers[self.packetloc].is_active():
            self.packetcost += self.lasers[self.packetloc].cost()
        self.steplasers()
    def is_safe_after(self, delay):
        for laser in self.lasers.values():
            if not laser.is_safe_after(delay):
                print(f'broke on {laser.depth}')
                return False
        return True
firewall = Firewall()
filename = 'input.txt'
with open(filename) as infile:
    for line in infile.readlines():
        parts = [int(part) for part in line.strip().split(': ')]
        toadd_laser = Laser(parts[0], parts[1])
        firewall.add_laser(toadd_laser)
for i in range(100):
    firewall.step()
print(firewall.packetcost)

laserdict = {}
with open(filename) as infile:
    for line in infile.readlines():
        parts = [int(part) for part in line.strip().split(': ')]
        laserdict[parts[0]] = parts[1]


f = Firewall()
for depth, _range in laserdict.items():
    f.add_laser(Laser(depth, _range))
f.is_safe_after(1)
for delay in range(1000000, 10000000):
    if f.is_safe_after(delay):
        print(delay)
        3 / 0
    else:
        # print(f'd={delay}')
        pass
