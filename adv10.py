def part1(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    pipes = {
        '|': (1, 1, 0, 0), 
        '-': (0, 0, 1, 1),
        'L': (1, 0, 1, 0),
        'J': (1, 0, 0, 1),
        '7': (0, 1, 0, 1),
        'F': (0, 1, 1, 0),
        '.': (0, 0, 0, 0)
        } 
    loop = []
    position = (0, 0)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'S':
                loop.append((i, j))
                position = (i, j)
                break
        else:
            continue
        break
    loop.append((position[0], position[1]+1))
    prevposition = loop[0]
    position = loop[-1]
    while position != loop[0]:
        newpositions = []
        pipe =  lines[position[0]][position[1]]
        if pipes[pipe][0]:
            newpositions.append((position[0]-1, position[1]))
        if pipes[pipe][1]:
            newpositions.append((position[0]+1, position[1]))
        if pipes[pipe][2]:
            newpositions.append((position[0], position[1]+1))
        if pipes[pipe][3]:
            newpositions.append((position[0], position[1]-1))
        for i in newpositions:
            if i != prevposition: 
                prevposition = position
                position = i
                loop.append(position)
                break
    # print(loop)
    print(len(loop)//2)
            
from bitarray import bitarray as ba        
    
def part2(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    pipes = {
        '|': (1, 1, 0, 0), 
        '-': (0, 0, 1, 1),
        'L': (1, 0, 1, 0),
        'J': (1, 0, 0, 1),
        '7': (0, 1, 0, 1),
        'F': (0, 1, 1, 0),
        '.': (0, 0, 0, 0)
        } 
    loop = []
    position = (0, 0)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'S':
                loop.append((i, j))
                position = (i, j)
                break
        else:
            continue
        break
    loop.append((position[0], position[1]+1))
    prevposition = loop[0]
    position = loop[-1]
    while position != loop[0]:
        newpositions = []
        pipe =  lines[position[0]][position[1]]
        if pipes[pipe][0]:
            newpositions.append((position[0]-1, position[1]))
        if pipes[pipe][1]:
            newpositions.append((position[0]+1, position[1]))
        if pipes[pipe][2]:
            newpositions.append((position[0], position[1]+1))
        if pipes[pipe][3]:
            newpositions.append((position[0], position[1]-1))
        for i in newpositions:
            if i != prevposition: 
                prevposition = position
                position = i
                loop.append(position)
                break
    q = ['|', 'J', 'L']
    output = 0
    for i in range(len(lines)):
        for j in range(0, len(lines[0])):
            if (i, j) in loop:
                continue
            count = 0
            for l in range(j-1, -1, -1):
                char = lines[i][l]
                if (char in q) and ((i, l) in loop): count += 1
            if count % 2 == 1:
                output += 1
    print(output)
                    
        
        
        
    
part2('input')