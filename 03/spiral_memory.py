def get_level(cell):
    i = 0
    while cell > (2*i+1)**2:
        i += 1
    return i
def find_coord(cell):
    level = get_level(cell)
    x = level
    y = -level
    current = (2*level+1)**2
    while x != -level:
        if current == cell:
            return (x, y)
        x-=1
        current -= 1
    while y != level:
        if current == cell:
            return (x, y)
        y+=1
        current -= 1
    while x != level:
        if current == cell:
            return (x, y)
        x+=1
        current -= 1
    while y != -level:
        if current == cell:
            return (x, y)
        y-=1
        current -= 1
    return None
print(find_coord(347991))
