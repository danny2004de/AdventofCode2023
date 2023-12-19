import math
def part1(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    seeds = list(map(int, lines[0].split(': ')[1].split()))
    maps = []
    for i in range(2, len(lines)):
        if ':' in lines[i]:
            tempmap = {}
        elif len(lines[i]) == 0:
            maps.append(tempmap)
        else:
            nums = list(map(int, lines[i].split()))
            tempmap[nums[1]] = (nums[0], nums[2])
            if (i == len(lines) - 1): maps.append(tempmap)
    locations = []
    for seed in seeds:
        temp = seed
        for m in maps:
            # b = False
            for k in m.keys():
                if temp - k < m[k][1] and temp >= k:
                    temp = m[k][0] + temp - k
                    break
        locations.append(temp)
    print(min(locations))
# def part2(filename):
#     f = open(filename, 'r')
#     lines = f.read().splitlines()
#     line0nums = list(map(int, lines[0].split(': ')[1].split()))
#     it = iter(line0nums)
#     seeds = zip(it, it)
#     maps = []
#     for i in range(2, len(lines)):
#         if ':' in lines[i]:
#             tempmap = {}
#         elif len(lines[i]) == 0:
#             maps.append(tempmap)
#         else:
#             nums = list(map(int, lines[i].split()))
#             tempmap[nums[1]] = (nums[0], nums[2])
#             if (i == len(lines) - 1): maps.append(tempmap)
#     # locations = []
#     minimum = math.inf
#     for seed in seeds:
#         # temploc = []
#         for i in range(seed[1]):
#             temp = seed[0]+i
#             for m in maps:
#                 # b = False
#                 for k in m.keys():
#                     if temp - k < m[k][1] and temp >= k:
#                         b = True
#                         temp = m[k][0] + temp - k
#                         break
#             # temploc.append(temp)
#             minimum = min(minimum, temp)
#         # locations.append(min(temploc))
#     print(minimum)

def part2(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    line0nums = list(map(int, lines[0].split(': ')[1].split()))
    it = iter(line0nums)
    seeds = zip(it, it)
    seeds = sorted(seeds)
    maps = []
    for i in range(2, len(lines)):
        if ':' in lines[i]:
            tempmap = []
        elif len(lines[i]) == 0:
            maps.append(tempmap)
        else:
            nums = tuple(map(int, lines[i].split()))
            tempmap.append(nums)
    maps.append(tempmap)

    for m in maps:
        mappedintervals = []
        for seedstart, intlen in seeds:
            while intlen != 0:
                intfound = False
                intnotmapped = intlen
                for dest, source, r in m:
                    if source <= seedstart < source + r:
                        offset = seedstart - source
                        r1 = min(r - offset, intlen)
                        mappedintervals.append((dest+offset, r1))
                        seedstart += r1
                        intlen -= r1
                        intfound = True
                        break
                    else:
                        if seedstart < source:
                            intnotmapped = min(intnotmapped, source - seedstart)
                if not intfound:
                    h = min(intnotmapped, intlen)
                    mappedintervals.append((seedstart, h))
                    seedstart += h
                    intlen -= h
        seeds = mappedintervals
    print(min(seeds))
                        
    #     for m in maps
    # locations = []
    # minimum = math.inf
    # for seed in seeds:
    #     # temploc = []
    #     for i in range(seed[1]):
    #         temp = seed[0]+i
    #         for m in maps:
    #             # b = False
    #             for k in m.keys():
    #                 if temp - k < m[k][1] and temp >= k:
    #                     b = True
    #                     temp = m[k][0] + temp - k
    #                     break
    #         # temploc.append(temp)
    #         minimum = min(minimum, temp)
    #     # locations.append(min(temploc))
    # print(minimum)


    
    
# part1('input')
part2('input')