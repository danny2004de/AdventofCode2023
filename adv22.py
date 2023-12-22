def part1(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    bricks = []
    for line in lines:
        line = line.split('~')
        a = tuple(map(int, line[0].split(',')))
        b = tuple(map(int, line[1].split(',')))
        bricks.append((a, b))
    def findminz(i):
        return i[0][2]
    sortedbricks = bricks.copy()
    sortedbricks.sort(key=findminz)
    extrudedbricks = []
    for a,b in sortedbricks:
        cells = []
        for x in range(a[0], b[0]+1):
            for y in range(a[1], b[1]+1):
                for z in range(a[2], b[2]+1):
                    cells.append((x,y,z))
        extrudedbricks.append(cells)
    def drop():
        dropped = set(range(len(extrudedbricks)))
        ground = set()
        for i, b in enumerate(extrudedbricks):
            lowest = [(x,y,z) for x,y,z in b if z == b[0][2]]
            if b[0][2] == 1:
                dropped.remove(i)
                for bb in b:
                    ground.add(bb)
            elif any((v[0], v[1], v[2]-1) in ground for v in lowest):
                dropped.remove(i)
                for bb in b:
                    ground.add(bb)
            else:
                l = [(bb[0], bb[1], bb[2]-1) for bb in b]
                extrudedbricks[i] = l
        return len(dropped)
    d = drop()
    while d > 0:
        d = drop()
    tempbricks = extrudedbricks.copy()
    safe = []
    for b in tempbricks:
        extrudedbricks.remove(b)
        d = drop()
        if d == 0:
            safe.append(b)
        extrudedbricks = tempbricks.copy()
    print(len(safe))

def part2(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    bricks = []
    for line in lines:
        line = line.split('~')
        a = tuple(map(int, line[0].split(',')))
        b = tuple(map(int, line[1].split(',')))
        bricks.append((a, b))
    def findminz(i):
        return i[0][2]
    sortedbricks = bricks.copy()
    sortedbricks.sort(key=findminz)
    extrudedbricks = []
    for a,b in sortedbricks:
        cells = []
        for x in range(a[0], b[0]+1):
            for y in range(a[1], b[1]+1):
                for z in range(a[2], b[2]+1):
                    cells.append((x,y,z))
        extrudedbricks.append(cells)
    def drop():
        dropped = set(range(len(extrudedbricks)))
        ground = set()
        for i, b in enumerate(extrudedbricks):
            lowest = [(x,y,z) for x,y,z in b if z == b[0][2]]
            if b[0][2] == 1:
                dropped.remove(i)
                for bb in b:
                    ground.add(bb)
            elif any((v[0], v[1], v[2]-1) in ground for v in lowest):
                dropped.remove(i)
                for bb in b:
                    ground.add(bb)
            else:
                l = [(bb[0], bb[1], bb[2]-1) for bb in b]
                extrudedbricks[i] = l
        return len(dropped)
    d = drop()
    while d > 0:
        d = drop()
    tempbricks = extrudedbricks.copy()
    ans = 0
    for b in tempbricks:
        extrudedbricks.remove(b)
        ans += drop()
        extrudedbricks = tempbricks.copy()
    print(ans)
        
part1('input')
part2('input')