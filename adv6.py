def part1(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    times = list(map(int, list(lines[0].split(':')[1].split())))
    distances = list(map(int, list(lines[1].split(':')[1].split())))
    races = zip(times, distances)
    prod = 1
    for time, distance in races:
        count = 0
        for t in range(time+1):
            velocity = t
            d = velocity * (time-t)
            if d > distance:
                count += 1
        prod *= count
    print(prod)
    

def part2(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    times = list(lines[0].split(':')[1].split())
    time = int(''.join(times))
    distances = list(lines[1].split(':')[1].split())
    distance = int(''.join(distances))
    shortest = 0
    longest = 0
    for t in range(time+1):
        velocity = t
        d = velocity * (time-t)
        if d > distance:
            shortest = t
            break
    for t in range(time, -1, -1):
        velocity = t
        d = velocity * (time-t)
        if d > distance:
            longest = t
            break
    print(longest - shortest + 1)

# part1('input')
part2('input')