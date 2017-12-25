def is_valid_pass_list(lst):
    for idx, item in enumerate(lst):
        if item in lst[idx+1:]:
            return False
    print(lst)
    return True


def is_valid_first_line(line):
    parts = line.strip().split(' ')
    return is_valid_pass_list(parts)

def is_valid_second_line(line):
    words = [str(sorted(word)) for word in line.strip().split(' ')]
    return is_valid_pass_list(words)

total = 0
second = 0
with open('input.txt') as passfile:
    for line in passfile.readlines():
        total += is_valid_first_line(line)
        second += is_valid_second_line(line)
print(total)
print(second)
