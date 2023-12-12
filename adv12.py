from functools import cache
def part1(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    s = 0
    def calculate(line):
        a = line.split()
        runlengths = list(map(int, a[1].split(',')))
        springs = a[0] + '.'
        @cache
        def dp(index, runs, runlen, combs = 0):
            if index >= len(springs): 
                return (runs == len(runlengths) and runlen == 0)
            if runs > len(runlengths): return 0
            if springs[index] in '.?':
                if runlen == 0 or runlen == runlengths[runs-1]:
                    combs += dp(index + 1, runs, 0)
            if springs[index] in '?#':
                if runlen == 0:
                    combs += dp(index + 1, runs + 1, 1)
                else:
                    combs += dp(index + 1, runs, runlen + 1)
            return combs
        return dp(0, 0, 0)
            
    for line in lines:
        s += calculate(line)
    print(s)
    
def part2(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    s = 0
    def calculate(line):
        a = line.split()
        runlengths = list(map(int, a[1].split(',')))*5
        springs = (a[0]+'?')*4+a[0] + '.'
        @cache
        def dp(index, runs, runlen, combs = 0):
            if index >= len(springs): 
                return (runs == len(runlengths) and runlen == 0)
            if runs > len(runlengths): return 0
            if springs[index] in '.?':
                if runlen == 0 or runlen == runlengths[runs-1]:
                    combs += dp(index + 1, runs, 0)
            if springs[index] in '?#':
                if runlen == 0:
                    combs += dp(index + 1, runs + 1, 1)
                else:
                    combs += dp(index + 1, runs, runlen + 1)
            return combs
        return dp(0, 0, 0)
            
    for line in lines:
        s += calculate(line)
    print(s)
    
    
part1('input')
part2('input')

# def part1(filename):
#     f = open(filename, 'r')
#     lines = f.read().splitlines()
#     s = 0
#     for line in lines:
#         a = line.split()
#         nums = list(map(int, a[1].split(',')))
#         springs = a[0] + '.'
#         n = len(nums)
#         nums.append(len(springs)+1)
#         arr = {}
#         arr[(0, 0, 0)] = 1
#         for i in range(len(springs)):
#             for j in range(n+1):
#                 for p in range(len(springs)+1):
#                     c = arr.get((i, j, p), 0)
#                     if not c: continue
#                     if springs[i] == '.' or springs[i] == '?':
#                         if p == 0 or p == nums[j - 1]:
#                             arr[(i+1, j, 0)] = c + arr.get((i+1, j, 0), 0)
#                     if springs[i] == '#' or springs[i] == '?':
#                         if p == 0:
#                             arr[(i+1, j+1 , p+1)] = c + arr.get((i+1, j+1, p+1), 0)
#                         else:
#                             arr[(i+1, j , p+1)] = c + arr.get((i+1, j, p+1), 0)
#         s += arr[(len(springs), n, 0)]

#     print(s)
        

# def part2(filename):
#     f = open(filename, 'r')
#     lines = f.read().splitlines()
#     s = 0
#     for line in lines:
#         a = line.split()
#         nums = list(map(int, a[1].split(',')))
#         springs = (a[0] + '?')*4 + a[0] + '.'
#         nums = nums*5
#         n = len(nums)
#         nums.append(len(springs)+1)
#         arr = {}
#         arr[(0, 0, 0)] = 1
#         for i in range(len(springs)):
#             for j in range(n+1):
#                 for p in range(len(springs)+1):
#                     c = arr.get((i, j, p), 0)
#                     if not c: continue
#                     if springs[i] == '.' or springs[i] == '?':
#                         if p == 0 or p == nums[j - 1]:
#                             arr[(i+1, j, 0)] = c + arr.get((i+1, j, 0), 0)
#                     if springs[i] == '#' or springs[i] == '?':
#                         if p == 0:
#                             arr[(i+1, j+1 , p+1)] = c + arr.get((i+1, j+1, p+1), 0)
#                         else:
#                             arr[(i+1, j , p+1)] = c + arr.get((i+1, j, p+1), 0)
#         s += arr[(len(springs), n, 0)]
#     print(s)

# part1('input')
# part2('input')