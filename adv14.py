def part1(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    lines = list(map(list, zip(*lines)))
    s = 0
    for line in lines:
        weight = len(line)
        for i, char in enumerate(line):
            if char == 'O':
                s += weight
                weight -= 1
            if char == '#':
                weight = len(line) - i - 1
    print(s)
    
def part2(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    def cycle(lines, n):
        for __ in range(n):
            for _ in range(4):
                lines = list(zip(*reversed(lines)))
                lines = ["".join(i).split("#") for i in lines]
                for i in range(len(lines)):
                    for j in range(len(lines[i])):
                        lines[i][j] = sorted(lines[i][j])

                new = []
                for i in lines:
                    temp = []
                    for j in i:
                        if not j:
                            temp.append("#")
                            continue
                        else:
                            temp += j
                            temp += ["#"]
                    new.append(temp[:-1])
                lines = new
        return lines

    lines = cycle(lines, 1000)
    lines = list(zip(*reversed(lines)))
    ans = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "O":
                ans += j + 1

    print(ans)
    

part1('input')
part2('input')