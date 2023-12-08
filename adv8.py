def part1(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    d = {'R':1, 'L':0}
    instructions = lines[0]
    locs = {}
    for i in range(2, len(lines)):
        x = lines[i].split(' = ')
        locs[x[0]] = (x[1][1:4], x[1][6:9])
    k = 'AAA'
    counter = 0
    while (k != 'ZZZ'):
        for i in instructions:
            k = locs[k][d[i]]
            counter += 1
            if k == 'ZZZ':
                break
    print(counter)

import math

def part2(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    d = {'R':1, 'L':0}
    instructions = lines[0]
    locs = {}
    starts = []
    for i in range(2, len(lines)):
        x = lines[i].split(' = ')
        locs[x[0]] = (x[1][1:4], x[1][6:9])
        if x[0][-1] == 'A':
            starts.append(x[0])
    def simulate (start):
        counter = 0
        position = start
        while True:
            for i in instructions:
                position = locs[position][d[i]]
                counter += 1
                if position[-1] == 'Z': return counter
    positions = set(starts)      
    times = list(map(simulate, positions))
    print(math.lcm(*times))
    
# part1('input')
part2('input')