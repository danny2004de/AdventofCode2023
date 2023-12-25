from heapq import heappush, heappop
from collections import Counter
def part1(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    components = {}
    for line in lines:
        key, connections = line.split(': ')
        connections = connections.split()
        for c in connections:
            if key in components:
                components[key].append(c)
            else:
                components[key] = [c]
            if c in components:
                components[c].append(key)
            else:
                components[c] = [key]
    # modes = Counter({c:0 for c in components})
    # def gotostart(v, start):
    #     if v == start:
    #         return
    #     modes[v] += 1
    #     gotostart(prev[v], start)
    # for start in list(components.keys())[0:100]:
    #     dist = {c:1e100 for c in components}
    #     prev = {c:'' for c in components}
    #     dist[start] = 0
    #     q = [(0, start)]
    #     seen = set()
    #     while q:
    #         d, u = heappop(q)
    #         if u in seen:
    #             continue
    #         seen.add(u)
    #         for v in components[u]:
    #             alt = d + 1
    #             if alt < dist[v]:
    #                 dist[v] = alt
    #                 prev[v] = u
    #                 heappush(q, (alt, v))
        # for c in components:
        #     gotostart(c, start)
    # k = Counter(modes)
    # high = k.most_common(6)
    # for a, b in high:
    #     print(a, components[a])
    components['clb'].remove('brd')
    components['brd'].remove('clb')
    components['glz'].remove('mxd')
    components['mxd'].remove('glz')
    components['bbz'].remove('jxd')
    components['jxd'].remove('bbz')
    q = ['clb']
    s = set()
    def find_group(v):
        s.add(v)
        for n in components[v]:
            if n in s:
                continue
            q.append(n)
    while len(q):
        u = q.pop()
        find_group(u)
    set1 = s.copy()
    s = set()
    q = ['brd']
    while len(q):
        u = q.pop()
        find_group(u)
    set2 = s.copy()
    print(len(components))
    print(len(set1))
    print(len(set2))
    print(len(set1)*len(set2))

def part2(filename): 
    print('merry christmas!')
    
part1('input')
part2('input')