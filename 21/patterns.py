import re
import copy
import math

def hash_value(lst):
    _max = 0
    for i in range(4):
        lst = list(zip(*reversed(lst)))
        _sum = sum(lst)
        if _sum > _max:
            _max = _sum
    lst = [x[::-1] for x in lst]
    for i in range(4):
        lst = list(zip(*reversed(lst)))
        _sum = sum(lst)
        if _sum > _max:
            _max = _sum
    return _max

def sum(lst):
    _sum = 0
    for idx, element in enumerate([y for x in lst for y in x]):
        if element:
            _sum += 2**idx
    return _sum

class Rule(object):
    def __init__(self, input, output):
        self.input = hash_value(input)
        self.output = output
        self.size = len(input)

def to_list_of_lists(instr):
    return [[0 if char == '.' else 1 for char in row] for row in instr.split('/')]

def get_subsquare(to_enhance, i, j, length):
    subarray = to_enhance[i*length:i*length+length]
    return [sub[j*length:j*length+length] for sub in subarray]

def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]

def flatten(lst, result_len, size):
    # (f'FLATTEN: {lst}')
    result = [['A' for i in range(result_len)] for j in range(result_len)]
    # for square in lst:
    #     for row in square:
    #         (row)
    # (result_len)
    # (size)
    for i in range(result_len):
        for j in range(result_len):
            x, y = (i // size), (j // size)
            square_idx = x * (result_len//size) + y
            result[i][j] = lst[square_idx][i%size][j%size]

    # for idx, i in enumerate(lst):
    #     print(i)
    #     for jdx, j in enumerate(i):
    #         print(str(idx) + ' ' + str(j))
    #         result.append(j)
    # print(f'RESULT_FLATTEN: {result}')
    return result

def enhance(to_enhance, rules):
    total_size = len(to_enhance)
    result = []
    for size in [2,3]:
        if total_size % size == 0:
            result_len = total_size + (total_size // size)
            square_size = size + 1
            # print(f'divisible by {size}')
            for i in range(total_size // size):
                for j in range(total_size // size):
                    square = get_subsquare(to_enhance, i, j, size)
                    result.append(replace(square, rules))
            return flatten(result, result_len, square_size)


def replace(subsquare, rules):
    hashed = hash_value(subsquare)
    for rule in rules:
        if rule.input == hashed:
            # print('found match')
            retval = copy.deepcopy(rule.output)
            # print(retval)
            return retval

rules = []
with open('input.txt') as infile:
    for line in infile.readlines():
        t_input, t_output = re.split(' => ', line.strip())
        l_input, l_output = to_list_of_lists(t_input), to_list_of_lists(t_output)
        rule = Rule(l_input, l_output)
        rules.append(rule)
        # print(rule.input)

to_enhance = to_list_of_lists('.#./..#/###')
for i in range(18):
    to_enhance = enhance(to_enhance, rules)
    print(f'ENHANCED: {to_enhance}')

total = 0
for row in to_enhance:
    total += row.count(1)
print(total)
