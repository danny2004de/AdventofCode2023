import numpy as np
def part1(filename): 
    maxdistance = 64
    f = open(filename, 'r')
    lines = f.read().splitlines()
    directions = {'right': (0, 1), 'up': (-1, 0), 'down': (1, 0), 'left': (0, -1)}
    for i, l in enumerate(lines):
        for j, char in enumerate(l):
            if char == 'S':
                start = (i, j)
                break
        else:
            continue
        break
    distances = np.full((len(lines), len(lines[0])), -1)
    def find_distances(position, distance):
        x,y = position
        if (x not in range(len(lines))) or (y not in range(len(lines[0]))):
            return
        char = lines[x][y]
        if char == '#':
            return
        if distances[x][y] >= 0 and distance >= distances[x][y]:
            return
        distances[x][y] = distance
        if distance == maxdistance: 
            return
        for u, v in directions.values():
            find_distances((x+u, y+v), distance+1)
    find_distances(start, 0)
    c = np.where(distances % 2 == 0, 1, 0)
    print(c.sum())

def part2(filename): 
    goal = 26501365
    f = open(filename, 'r')
    lines = f.read().splitlines()
    directions = {'right': (0, 1), 'up': (-1, 0), 'down': (1, 0), 'left': (0, -1)}
    for i, l in enumerate(lines):
        for j, char in enumerate(l):
            if char == 'S':
                start = (i, j)
                break
        else:
            continue
        break
    def find_nums():
        points = set()
        points.add(start)
        nums = []
        for distance in range(1, 100000):
            temp = set()
            for i,j in points:
                for k in directions.values():
                    u = i + k[0]
                    v = j + k[1]
                    if lines[u%len(lines)][v%len(lines)] != '#':
                        temp.add((u,v))
            if distance%len(lines) == goal%len(lines):
                nums.append(len(temp))
                if len(nums) == 3:
                    break
            points = temp
        return nums
    nums = find_nums()
    # nums = [3835, 34125, 94603]
    def f(n):
        a = nums[0]
        c = (nums[2] + nums[0] - 2*nums[1])//2
        b = nums[1] - nums[0] - c
        # print(a,b,c)
        return a + b*n + c*(n**2)
    print(f(goal//len(lines)))
    
part1('input')
part2('input')