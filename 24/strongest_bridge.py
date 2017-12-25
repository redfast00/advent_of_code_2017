bridgelist = []
with open('input.txt') as infile:
    for line in infile.readlines():
        i, o = line.strip().split('/')
        i, o = int(i), int(o)
        bridgelist.append((i,o,))

def build_bridge(bridgelist, already_used=None, current_value=0, connector_used=0):
    if already_used == None:
        already_used = ((0,0),)
    cur_max = 0
    for candidate in filter(lambda x: connector_used in x, bridgelist):
        if candidate not in already_used:
            begin, end = candidate
            connects_to = end if begin == connector_used else begin
            used_now = already_used + (candidate,)
            value = build_bridge(bridgelist, already_used=used_now, current_value=(current_value+sum(candidate)), connector_used=connects_to)
            if value > cur_max:
                cur_max = value
    if cur_max != 0:
        return cur_max
    else:
        print('Found end of bridge')
        return current_value

print(build_bridge(bridgelist))
