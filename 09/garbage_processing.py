def remove_garbage(garbage_str):
    result = ''
    in_garbage = False
    ignore = False
    total_garbage = 0
    for idx, i in enumerate(garbage_str):
        if ignore:
            ignore = False
        elif i == '>':
            in_garbage = False
        elif in_garbage and i == '!':
            ignore = True
        elif in_garbage:
            total_garbage += 1
        elif i == '<':
            in_garbage = True
        elif not in_garbage:
            result += i
        else:
            print(f"found: '{i}' at {idx}")
    return result, total_garbage

def fuk_up_some_commas(instr):
    result = instr.replace('{,', '{').replace(',}', '}')
    while result != instr:
        instr = result
        result = instr.replace('{,', '{').replace(',}', '}')
    return result

def score(inpt, level=1):
    return level + sum([score(i, level=level+1) for i in inpt])
with open("input.txt") as infile:
    line = infile.readline().strip()
    result, garb = remove_garbage(line)
    result = fuk_up_some_commas(result)
    listoflists = eval(result.replace('{','[').replace('}',']'))
    print(score(listoflists))
    print(garb)


# with open("garbage.txt") as garbfile:
#     for line in garbfile.readlines():
#         assert '' == remove_garbage(line.strip())
