import re
from collections import namedtuple
Node = namedtuple('Node', ['children', 'weight'])
def is_root(tree, candidate):
    for k, value in tree.items():
        if value.children is not None and candidate in value.children:
            return False
    return True

with open('input.txt') as infile:
    tree = {}
    for line in infile.readlines():
        line = line.strip()
        parts = line.split(' -> ')
        m = re.match(r'([a-z]+) \((\d+)\)', parts[0])
        if len(parts) == 2:
            nodes = parts[1].split(', ')
        else:
            nodes = None
        tree[m.group(1)] = Node(nodes, int(m.group(2)))
    root = ''
    for k in tree:
        if is_root(tree, k):
            print(k)
            root = k
    def sum_tree(nodename):
        current = tree[nodename]
        if current.children is None:
            return current.weight
        else:
            results = list(map(sum_tree, current.children))
            # check if weights are same
            if results.count(results[0]) != len(results):
                print(f"balancing error in {nodename}")
                print(current.children)
                print(results)
            return sum(results) + current.weight
    sum_tree(root)
