from collections import deque
import numpy as np
def part1(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    directions = {'right': (0, 1), 'up': (-1, 0), 'down': (1, 0), 'left': (0, -1)}
    direction = directions['right']
    # q = deque()
    q = []
    visited = np.zeros((len(lines), len(lines[0])))
    ds = {}
    position = (0, -1)
    q.append((direction, position))
    while len(q):
        direction, position = q.pop()
        i, j = tuple([sum(x) for x in zip(direction, position)])
        if (i not in range(len(lines))) or (j not in range(len(lines))): continue
        char = lines[i][j]
        visited[i][j] = 1
        if (i, j) in ds:
            if direction in ds[(i,j)]: continue
            ds[(i,j)].append(direction)
        else: 
            ds[(i, j)] = [direction]
        if char == '/':
            if direction == directions['up']: q.append((directions['right'], (i, j)))
            elif direction == directions['down']: q.append((directions['left'], (i, j)))
            elif direction == directions['left']: q.append((directions['down'], (i, j)))
            elif direction == directions['right']: q.append((directions['up'], (i, j)))
        elif char == '\\':
            if direction == directions['up']: q.append((directions['left'], (i, j)))
            elif direction == directions['down']: q.append((directions['right'], (i, j)))
            elif direction == directions['left']: q.append((directions['up'], (i, j)))
            elif direction == directions['right']: q.append((directions['down'], (i, j)))
        elif char == '-':
            if direction == directions['up'] or direction == directions['down']:
                q.append((directions['left'], (i, j)))
                q.append((directions['right'], (i, j)))
            else: q.append((direction, (i, j)))
        elif char == '|':
            if direction == directions['left'] or direction == directions['right']:
                q.append((directions['up'], (i, j)))
                q.append((directions['down'], (i, j)))
            else: q.append((direction, (i, j)))
        else:
            q.append((direction, (i, j)))
    print(np.sum(visited))
            
        
    
    
def part2(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    
part1('input')