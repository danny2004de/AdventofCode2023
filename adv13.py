def parse_input(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    patterns = []
    p = []
    for line in lines:
        if line != '':
            p.append(line)
        else: 
            patterns.append(p)
            p = []
    patterns.append(p)
    return patterns

def find_horizontal(pattern):
    for i in range(len(pattern)-1):
        half1 = pattern[:i+1]
        half2 = pattern[i+1:]
        half1.reverse()
        for j in range(min(len(half1), len(half2))):
            if half1[j] != half2[j]: break
        else:
            return i+1
    return 0

def find_vertical(pattern):
    pattern = list(map(list, zip(*pattern)))
    return find_horizontal(pattern)

def find_smudge_horizontal(pattern):
    for i in range(len(pattern)-1):
        half1 = pattern[:i+1]
        half2 = pattern[i+1:]
        half1.reverse()
        discrepancies = 0
        for j in range(min(len(half1), len(half2))):
            if half1[j] != half2[j]: 
                discrepancies += sum(1 for a, b in zip(half1[j], half2[j]) if a != b) 
        if discrepancies == 1:
            return i+1
    return 0     

def find_smudge_vertical(pattern):
    pattern = list(map(list, zip(*pattern)))
    return find_smudge_horizontal(pattern)       

def part1(filename): 
    patterns = parse_input(filename)        
    s = 0
    for p in patterns:
        s += find_horizontal(p)*100
        s += find_vertical(p)
    print(s)
    
def part2(filename):
    patterns = parse_input(filename)
    s = 0
    for p in patterns:
        s += find_smudge_horizontal(p)*100
        s += find_smudge_vertical(p)
    print(s)     
    
part1('input')
part2('input')