def part1(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    minpos = 200000000000000
    maxpos = 400000000000000
    hailstones = []
    for l in lines:
        l = l.split(' @ ')
        pos = tuple(map(int, l[0].split(', ')))
        velocity = tuple(map(int, l[1].split(', '))) 
        hailstones.append((pos, velocity))
    for i, (pos, vel) in enumerate(hailstones):
        x,y,z = pos
        vx,vy,vz = vel
        if x in range(minpos, maxpos+1) and y in range(minpos, maxpos+1):
            continue
        if x < minpos:
            t1 = (minpos - x)/vx
        elif x > maxpos:
            t1 = (maxpos - x)/vx
        else: t1 = 0
        if y < minpos:
            t2 = (minpos - y)/vy
        elif y > maxpos:
            t2 = (maxpos - y)/vy
        else: t2 = 0
        t = max(t1, t2)
        x = x + vx*t
        y = y + vy*t
        z = z + vz*t
        hailstones[i] = ((x,y,z), (vx,vy,vz))
    finalpositions = []
    for i, ((x, y, z), (vx, vy, vz)) in enumerate(hailstones):
        if vx > 0:
            t1 = (maxpos - x)/vx
        else:
            t1 = (minpos - x)/vx
        if vy > 0:
            t2 = (maxpos - y)/vy
        else:
            t2 = (minpos - y)/vy
        t = min(t1, t2)
        fx = x + vx*t
        fy = y + vy*t
        fz = z + vz*t
        finalpositions.append((fx,fy,fz))
    def ccw(A, B, C):
        # returns whether points A, B, C are in ccw order
        x = (C[1]-A[1])*(B[0]-A[0]) - (B[1]-A[1])*(C[0]-A[0])
        if x == 0: return x
        if x > 0: return 1
        else: return 2
    def onsegment(A, B, C):
        # checks if C is on AB
        return (C[0] <= max(A[0], B[0])) and (C[0] >= min(A[0], B[0])) and (C[1] <= max(A[1], B[1])) and (C[1] >= min(A[1], B[1]))
    def intersect(A, B, C, D):
        # returns whether AB and CD intersect
        o1 = ccw(A, C, D)
        o2 = ccw(B, C, D)
        o3 = ccw(A, B, C)
        o4 = ccw(A, B, D)
        if o1 != o2 and o3 != o4:
            return True
        if o1 == 0 and onsegment(C, D, A):
            return True
        if o2 == 0 and onsegment(C, D, B):
            return True
        if o3 == 0 and onsegment(A, B, C):
            return True
        if o4 == 0 and onsegment(A, B, D):
            return True
        return False
    intersections = 0
    for h1 in range(len(hailstones)-1):
        pos1 = hailstones[h1][0]
        fpos1 = finalpositions[h1]
        for h2 in range(h1+1, len(hailstones)):
            pos2 = hailstones[h2][0]
            fpos2 = finalpositions[h2]
            if intersect(pos1, fpos1, pos2, fpos2):
                intersections += 1
    print(intersections)     
    
from scipy.optimize import fsolve
def part2(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    minpos = 200000000000000
    maxpos = 400000000000000
    hailstones = []
    for l in lines:
        l = l.split(' @ ')
        pos = tuple(map(int, l[0].split(', ')))
        velocity = tuple(map(int, l[1].split(', '))) 
        hailstones.append((pos, velocity))
    def equations(p):
        x,y,z,vx,vy,vz = p
        ret = []
        for i in hailstones[1:4]:
            ((x1, y1, z1), (vx1, vy1, vz1)) = i
            ret.append((x-x1)*(vy-vy1) - (y-y1)*(vx-vx1))
            ret.append((x-x1)*(vz-vz1) - (z-z1)*(vx-vx1))
        return ret
    x,y,z,vx,vy,vz = fsolve(equations, hailstones[0][0]+hailstones[0][1])
    print(x+y+z)

part1('input')
part2('input')