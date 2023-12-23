from heapq import heappop, heappush
def part1(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    def inrange(position):
        return (position[0] in range(len(lines))) and (position[1] in range(len(lines[0])))
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    n = len(lines)
    mindist, maxdist = 1, 3
    start = (0,0)
    cost = 0
    banneddirection = -1
    q = [(cost, start, banneddirection)]
    costs = {}
    seen = set()
    while q:
        cost, position, banneddirection = heappop(q)
        x,y = position
        if x == n-1 and y == n-1:
            print(cost)
            return cost
        if (position, banneddirection) in seen:
            continue
        seen.add((position, banneddirection))
        for d, dir in enumerate(directions):
            costinc = 0
            if banneddirection in [d, (d+2)%4]:
                continue
            for distance in range(1, maxdist+1):
                u = x + dir[0]*distance
                v = y + dir[1]*distance
                if inrange((u,v)):
                    costinc += int(lines[u][v])
                    if distance < mindist:
                        continue
                    newcost = cost + costinc
                    if costs.get(((u,v), d), 1e100) <= newcost:
                        continue
                    costs[((u, v), d)] = newcost
                    heappush(q, (newcost, (u, v), d))
            
    
def part2(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    def inrange(position):
        return (position[0] in range(len(lines))) and (position[1] in range(len(lines[0])))
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    n = len(lines)
    mindist, maxdist = 4, 10
    start = (0,0)
    cost = 0
    banneddirection = -1
    q = [(cost, start, banneddirection)]
    costs = {}
    seen = set()
    while q:
        cost, position, banneddirection = heappop(q)
        x,y = position
        if x == n-1 and y == n-1:
            print(cost)
            return cost
        if (position, banneddirection) in seen:
            continue
        seen.add((position, banneddirection))
        for d, dir in enumerate(directions):
            costinc = 0
            if banneddirection in [d, (d+2)%4]:
                continue
            for distance in range(1, maxdist+1):
                u = x + dir[0]*distance
                v = y + dir[1]*distance
                if inrange((u,v)):
                    costinc += int(lines[u][v])
                    if distance < mindist:
                        continue
                    newcost = cost + costinc
                    if costs.get(((u,v), d), 1e100) <= newcost:
                        continue
                    costs[((u, v), d)] = newcost
                    heappush(q, (newcost, (u, v), d))
    
part1('input')
part2('input')