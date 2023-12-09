def part1(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    sum = 0
    for line in lines:
        histories = []
        history = list(map(int, line.split()))
        histories.append(history)
        while any(history):
            h = []
            for i in range(1, len(history)):
                h.append(history[i] - history[i-1])
            histories.append(h)
            history = h
        s = histories[-2][-1] + histories[-1][-1]
        for i in range(len(histories)-3, -1, -1):
            s = histories[i][-1] + s
        sum += s
    print(sum)        
def part2(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    sum = 0
    for line in lines:
        histories = []
        history = list(map(int, line.split()))
        histories.append(history)
        while any(history):
            h = []
            for i in range(1, len(history)):
                h.append(history[i] - history[i-1])
            histories.append(h)
            history = h
        s = histories[-2][0] - histories[-1][0]
        for i in range(len(histories)-3, -1, -1):
            s = histories[i][0] - s
        sum += s
    print(sum)     

part1('input')
part2('input')