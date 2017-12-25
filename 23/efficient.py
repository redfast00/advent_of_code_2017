b = 109300
c = 126300
import math

def is_prime(number):
    for i in range(2, int(math.sqrt(number)+1)):
        if number % i == 0:
            return False
    return True

total = 0
ctr = 0
while b != c:
    if not is_prime(b):
        total += 1
    b += 17
    ctr += 1
if not is_prime(b):
    total += 1
b += 17
ctr += 1

print(total)
print(ctr)
