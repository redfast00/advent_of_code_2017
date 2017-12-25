input_b = 109300
input_c = 126300

while True:
    enable_counter = False
    d = 2
    # SCHOOL
    e = 2
    # BACK
    if d * e == input_b:
        enable_counter = True
    # with e
    e += 1
    if e != input_b:
        jmp back
    # with d
    d += 1
    if d != input_b:
        jmp school
    if enable_counter:
        counter += 1
    if input_b  != input_c:
        input_b += 17
    else:
        break
