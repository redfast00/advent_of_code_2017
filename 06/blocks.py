class BlockRedistibutor(object):
    def __init__(self, blocks):
        self.states = []
        self.blocks = blocks
    def find_largest_block(self):
        return self.blocks.index(max(self.blocks))
    def step(self):
        current_state = self.blocks[:]
        if current_state in self.states:
            return False
        else:
            self.states.append(current_state)
        largest_block = self.find_largest_block()
        blocksize = self.blocks[largest_block]
        self.blocks[largest_block] = 0
        for i in range(blocksize):
            self.blocks[(largest_block+1+i)%len(self.blocks)] += 1
        return True
class SecondBlockRedistibutor(BlockRedistibutor):
    def find_index(self):
        return self.states.index(self.blocks)
with open('input.txt') as blockfile:
    blocks = [int(block) for block in blockfile.readline().strip().split('\t')]
    total = 0
    d = SecondBlockRedistibutor(blocks)
    while d.step():
        total += 1
    print(total)
    print(total - d.find_index())
