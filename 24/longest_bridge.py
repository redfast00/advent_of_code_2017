bridgelist = []
with open('input.txt') as infile:
    for line in infile.readlines():
        i, o = line.strip().split('/')
        i, o = int(i), int(o)
        bridgelist.append((i,o,))

maxlen = 0
maxstrength = 0
def build_bridge(bridgelist, already_used=None, current_value=0, connector_used=0, current_length=0):
    if already_used == None:
        already_used = ((0,0),)
    is_end = True
    local_max_length = 0
    local_max_strength = 0
    for candidate in filter(lambda x: connector_used in x, bridgelist):
        if candidate not in already_used:
            is_end = False
            begin, end = candidate
            connects_to = end if begin == connector_used else begin
            used_now = already_used + (candidate,)
            value, length = build_bridge(bridgelist, already_used=used_now, current_value=(current_value+sum(candidate)),
                                 connector_used=connects_to, current_length=current_length+1)

            # global maxlen
            # global maxstrength
            # if length > maxlen:
            #     maxlen = length
            #     maxstrength = value
            # elif length == maxlen:
            #     maxstrength = max(maxstrength, value)
            if length > local_max_length:
                local_max_length = length
                local_max_strength = value
            elif length == local_max_length:
                if value > local_max_strength:
                    local_max_strength = value
    if is_end:
        # print('Found end of bridge')
        return current_value, current_length
    else:
        return local_max_strength, local_max_length

print(build_bridge(bridgelist))
# print(maxlen, maxstrength)
