from vector import Vector
class Maze(object):
    def __init__(self, maze):
        self.maze = maze
        self.direction = Vector(1,0) # array index
        self.current_pos = Vector(0, self.maze[0].index('|'))
        self.moves = 1

    def get_char(self, vector):
        try:
            assert vector[0] >= 0 and vector[1] >= 0
            return self.maze[vector[0]][vector[1]]
        except:
            return ' '

    def next_direction(self):
        for i in range(2):
            direction = self.direction.rotate(90 + 180*i)
            if self.try_move_until_end(direction):
                self.direction = direction
                return True
        print("Not turned!")
        return False

    def try_move_until_end(self, direction):
        i = 1
        while True:
            char = self.get_char(self.current_pos + (direction * i))
            if char == ' ':
                return False
            elif char == '+' or char in 'TF':
                self.current_pos += (direction * i)
                print(f'{i}')
                self.moves += i
                return True
            elif char not in '-|':
                print(char)
            i += 1

with open('input.txt') as mazefile:
    maze = [list(line.rstrip('\n\r')) for line in mazefile.readlines()]
    m = Maze(maze)
    print(m.try_move_until_end(m.direction))
    while m.next_direction():
        pass
    print(m.current_pos)
    print(m.moves)
