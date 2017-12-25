input_b = 109300
input_c = 126300

while True:
    f = 1
    d = 2
    # SCHOOL
    e = 2
    # BACK
    g = d
    g *= e
    g -= b
    if g == 0:
        f = 0
    # with e
    e += 1
    g = e
    g -= b
    if g != 0:
        jmp back
    # with d
    d += 1
    g = d
    g -= b
    if g != 0:
        jmp school
    if f == 0:
        h += 1
    g = b
    g -= c
    if g == 0:
        b += 17
    else:
        break
