from vector import Vector
import re

def samesign(x, y, z):
    if x <= 0 and y <= 0 and z <= 0:
        return True
    if x >= 0 and y >= 0 and z >= 0:
        return True
    return False
class Particle(object):
    def __init__(self, location, velocity, acceleration, _id):
        self.location = location
        self.velocity = velocity
        self.acceleration = acceleration
        self._id = _id
    def step(self):
        self.velocity += self.acceleration
        self.location += self.velocity
    def distance(self):
        return abs(self.location[0]) + abs(self.location[1]) + abs(self.location[2])
    def interesting(self):
        for i in range(3):
            # boring
            if samesign(self.location[i], self.velocity[i], self.acceleration[i]):
                pass
            else:
                return True
        else:
            print(self.location, self.velocity, self.acceleration)
            return False
        return True
    def closest(self):
        _min = self.distance()
        while self.interesting():
            self.step()
            d = self.distance()
            if d < _min:
                _min = d
        self._min = _min
    def fastforward(self, steps):
        self.location += (steps * self.velocity ) + (self.acceleration * ((steps)*(steps+1)//2))
        self.velocity += steps*self.acceleration

def remove_collisions(particles):
    values = [particle.location.values for particle in particles]
    kept_particles = []
    for i, value in enumerate(values):
        if values.count(value) == 1:
            kept_particles.append(particles[i])
    return kept_particles
particles = []
with open("input.txt") as infile:
    for _id, line in enumerate(infile.readlines()):
        m = re.match('p=<([0-9-]*),([0-9-]*),([0-9-]*)>, v=<([0-9-]*),([0-9-]*),([0-9-]*)>, a=<([0-9-]*),([0-9-]*),([0-9-]*)>', line)
        l = Vector(int(m[1]), int(m[2]), int(m[3]))
        v = Vector(int(m[4]), int(m[5]), int(m[6]))
        a = Vector(int(m[7]), int(m[8]), int(m[9]))
        particles.append(Particle(l, v, a, _id))
    print("loaded")
    for i in range(5000):
        print(i)
        particles = remove_collisions(particles)
        for part in particles:
            part.step()
        # for i in range(1000):
        #     part.step()
    print(len(particles))
