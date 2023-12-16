def HASH(s):
    t = 0
    for c in s:
        t += ord(c)
        t *= 17
        t = t%256
    return t     

def part1(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    s = 0
    for line in lines:
        l = line.split(',')
        for x in l:
            s += HASH(x)    
    print(s)
    
def part2(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    s = 0
    boxes = [{} for ljlj in range(256)]
    for line in lines:
        l = line.split(',')
        for x in l:
            x = x.split('=')
            if len(x) == 2:
                label = x[0]
                box = HASH(label)
                boxes[box][label] = int(x[1])
            else: 
                x = x[0].split('-')
                label = x[0]
                box = HASH(label)
                if label in boxes[box]:
                    del boxes[box][label]
    for i, b in enumerate(boxes):
        for j, l in enumerate(b):
            s += (i+1)*(j+1)*(b[l])
    print(s)
part2('input')