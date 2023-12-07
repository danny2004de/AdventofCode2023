def part1(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    sum = 0
    for line in lines:
        line = line.split(': ')[1]
        line = line.split('|')
        wins = set(map(int, line[0].split()))
        mynums = list(map(int, line[1].split()))
        val = 0
        for i in mynums:
            if i in wins:
                val = val*2 if val > 0 else 1
        sum += val
    print(sum)
    
def part2(filename):
    matches = {}
    numcards = {}
    f = open(filename, 'r')
    lines = f.read().splitlines()
    for i in range(len(lines)):
        numcards[i] = 1
        line = lines[i].split(': ')[1]
        line = line.split('|')
        wins = set(map(int, line[0].split()))
        mynums = list(map(int, line[1].split()))
        for j in mynums:
            if j in wins:
                matches[i] = matches.get(i, 0) + 1
    i = 0
    while (i in numcards):
        for j in range(matches.get(i, 0)):
            try:
                numcards[j+i+1] = numcards[j+i+1] + numcards[i]
            except:
                break
        i += 1
    print(sum(numcards.values()))
    # print(matches)
        
part2('input')