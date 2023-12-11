
def part1(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    galaxies = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '#': galaxies.append((i, j))
    rows = set(range(len(lines)))
    cols = set(range(len(lines[0])))
    galrows = set([g[0] for g in galaxies])
    galcols = set([g[1] for g in galaxies])
    emptyrows = list(rows - galrows)
    emptycols = list(cols - galcols)
    sum = 0
    for galaxy1 in galaxies:
        for galaxy2 in galaxies:
            # if galaxy1 == galaxy2: continue
            distance = abs(galaxy2[0] - galaxy1[0]) + abs(galaxy2[1] - galaxy1[1])
            for i in emptyrows: 
                if i in range(min(galaxy1[0], galaxy2[0]), max(galaxy1[0], galaxy2[0])):
                    distance += 1
            for j in emptycols:
                if j in range(min(galaxy1[1], galaxy2[1]), max(galaxy1[1], galaxy2[1])):
                    distance += 1
            sum += distance
    print(sum//2)
 
    
def part2(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    galaxies = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '#': galaxies.append((i, j))
    rows = set(range(len(lines)))
    cols = set(range(len(lines[0])))
    galrows = set([g[0] for g in galaxies])
    galcols = set([g[1] for g in galaxies])
    emptyrows = list(rows - galrows)
    emptycols = list(cols - galcols)
    sum = 0
    for galaxy1 in galaxies:
        for galaxy2 in galaxies:
            # if galaxy1 == galaxy2: continue
            distance = abs(galaxy2[0] - galaxy1[0]) + abs(galaxy2[1] - galaxy1[1])
            for i in emptyrows: 
                if i in range(min(galaxy1[0], galaxy2[0]), max(galaxy1[0], galaxy2[0])):
                    distance += 1000000-1
            for j in emptycols:
                if j in range(min(galaxy1[1], galaxy2[1]), max(galaxy1[1], galaxy2[1])):
                    distance += 1000000-1
            sum += distance
    print(sum//2)
                         
# part1('input') 
part2('input')