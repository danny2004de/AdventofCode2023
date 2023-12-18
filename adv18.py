def part1(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    pos = (0, 0)
    perimeter = 0
    loop = [pos]
    dirs = {'L': (0, -1), 'U': (-1, 0), 'D': (1, 0), 'R': (0, 1)}
    for i, line in enumerate(lines):
        line = line.split()
        dir = dirs[line[0]] 
        steps = int(line[1])
        perimeter += steps
        pos = (pos[0] + dir[0]*steps, pos[1] + dir[1]*steps)
        loop.append(pos)
    area = 0
    for i, p in enumerate(loop):
        if i >= len(loop)-2:
            break
        q = loop[i+1]
        area += (p[0] + q[0])*(p[1] - q[1])
    print(area//2 + perimeter//2 + 1)

def part2(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    pos = (0, 0)
    loop = [(0, 0)]
    perimeter = 1
    dirs = {'2': (0, -1), '3': (-1, 0), '1': (1, 0), '0': (0, 1)}
    for i, line in enumerate(lines):
        line = line.split()
        dir = dirs[line[2][-2]] 
        steps = int(line[2][2:-2], 16)
        perimeter += steps
        pos = (pos[0] + dir[0]*steps, pos[1] + dir[1]*steps)
        loop.append(pos)
    area = 0
    for i, p in enumerate(loop):
        if i >= len(loop)-2:
            break
        q = loop[i+1]
        area += (p[0] + q[0])*(p[1] - q[1])
    print(area//2 + perimeter//2 + 1)

part1('input')
part2('input')
        