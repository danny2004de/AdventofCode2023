import numpy as np
def part1(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    directions = {'right': (0, 1), 'up': (-1, 0), 'down': (1, 0), 'left': (0, -1)}
    slides = {'>':(0, 1), '^':(-1, 0), 'v':(1,0), '<':(0,-1)}
    for i, char in enumerate(lines[0]):
        if char == '.':
            start = (0, i)
    visited = np.zeros((len(lines), len(lines[0])))
    distances = []
    def find_distances(position, distance, r):
        x,y = position
        if (x not in range(len(lines))) or (y not in range(len(lines[0]))):
            return
        if r[x][y]:
            return
        if x == len(lines)-1:
            distances.append(distance)
            return
        r[x][y] = 1
        char = lines[x][y]
        if char == '#':
            return
        if char == '.':
            for d in directions.values():
                u,v = d
                q.append(((x+u, y+v), distance+1, np.copy(r)))
        else:
            u,v = slides[char]
            q.append(((x+u, y+v), distance+1, np.copy(r)))
    q = [(start, 0, visited)]
    while len(q):
        s, t, r = q.pop()
        find_distances(s, t, r)
    print(max(distances))
        
def part2(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    directions = {'right': (0, 1), 'up': (-1, 0), 'down': (1, 0), 'left': (0, -1)}
    for i, char in enumerate(lines[0]):
        if char == '.':
            start = (0, i)
    def generate_adjacencies():
        ret = {}
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char != '#':
                    a = {}
                    for u, v in directions.values():
                        try:
                            if lines[i+u][j+v] != '#':
                                a[(i+u, j+v)] = 1
                        except IndexError:
                            continue
                    ret[(i,j)] = a
        points = list(ret.keys())
        for k in points:
            neighbors = ret[k]
            if len(neighbors) == 2:
                left, right = neighbors.keys()
                del ret[left][k]
                del ret[right][k]
                ret[left][right] = max(ret[left].get(right, 0), neighbors[left] + neighbors[right])
                ret[right][left] = ret[left][right]
                del ret[k]
        return ret
    adjacencies = generate_adjacencies()
    q = []
    best = 0
    visited = set()
    def find_distances(position, distance):
        nonlocal best
        if distance == -1:
            visited.remove(position)
            return
        if position[0] == len(lines)-1:
            best = max(best, distance)
            return
        if position in visited:
            return
        visited.add(position)
        q.append((position, -1))
        neighbors = adjacencies[position]
        for n in neighbors:
            d = distance + neighbors[n]
            q.append((n, d))
    q.append((start, 0))
    while len(q):
        s, t = q.pop()
        find_distances(s, t)
    print(best)

part1('input')
part2('input')