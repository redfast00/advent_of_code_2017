import re
class Merger():
    def __init__(self):
        self.connected = ['0']
        self.unconnected = []
    def add(self, lst):
        for item in lst:
            if item in self.connected:
                self.connected = list(set(self.connected + lst))
                return True
        else:
            self.unconnected.append(lst)
    def merge(self):
        still_unconnected = []
        for i in range(len(self.unconnected)):
            lst = self.unconnected.pop()
            for item in lst:
                if item in self.connected:
                    self.connected = list(set(self.connected + lst))
                    break
            else:
                still_unconnected.append(lst)
        self.unconnected = still_unconnected
        return len(self.connected)

    def keep_merging(self):
        self.connected = list(set(self.connected))
        while len(self.connected) != self.merge():
            self.connected = list(set(self.connected))

    def find_groups(self):
        i = 1
        self.keep_merging()
        print(len(self.connected))
        while len(self.unconnected) != 0:
            self.connected = [self.unconnected[0][0]]
            self.keep_merging()
            i += 1
        print(i)
merger = Merger()
with open('input.txt') as infile:
    for line in infile.readlines():
        parts = re.split(' <-> |, ',line.strip())
        merger.add(parts)
    merger.find_groups()
