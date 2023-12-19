def part1(filename):
    nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    ignore = nums.copy(); ignore.add('.')

    numstoadd = []
    f = open(filename, 'r')
    lines = f.read().splitlines()
    def search(top, bottom, left, right):
        for row in range(top, bottom+1):
            for col in range(left, right+1):
                char = lines[row][col]
                if char not in ignore:
                    return True
    top, bottom, left, right = 0, len(lines)-1, 0, len(lines[0])-1
    for i in range(len(lines)):
        founddigit = False
        num = ''
        for j in range(len(lines[0])):
            char = lines[i][j]
            if char in nums:
                num += char
                founddigit = True
                if j == right:
                    adjacent = search(max(i-1, 0), min(i+1, bottom), max(j-len(num), 0), min(j+1, right))
                    if adjacent: numstoadd.append(int(num))
            elif founddigit:
                founddigit = False
                adjacent = search(max(i-1, 0), min(i+1, bottom), max(j-len(num)-1, 0), min(j, right))
                if adjacent: numstoadd.append(int(num))
                num = ''
    print(sum(numstoadd))
    
def part2(filename):
    nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    # ignore = nums.copy(); ignore.add('.')
    
    f = open(filename, 'r')
    lines = f.read().splitlines()
    top, bottom, left, right = 0, len(lines)-1, 0, len(lines[0])-1
    def findratio(top, bottom, left, right):
        adjacentnums = []
        for i in range(top, bottom+1):
            j = left
            while j <= right:
                char = lines[i][j]
                if char in nums:
                    num = ''
                    k = j
                    while k > 0 and (lines[i][k-1] in nums): k -= 1
                    while k < len(lines[0]) and lines[i][k] in nums:
                        num += lines[i][k]
                        k += 1
                    adjacentnums.append(int(num))
                    j = min(k-1, right)
                j += 1
        if len(adjacentnums) == 2:
            return adjacentnums[0]*adjacentnums[1]
        return 0
                             
    sum = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            char = lines[i][j]
            if char == '*':
                sum += findratio(max(i-1, 0), min(i+1, bottom), max(j-1, 0), min(j+1, right))
    print(sum)
    
# part1('input')
part2('input')