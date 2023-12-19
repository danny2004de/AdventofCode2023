def part1(filename) :
    class game():
        def __init__(self, string):
            colors = {'red':0, 'green':1, 'blue':2}
            gameid, games = string.split(': ')
            self.gameid = int(gameid.split(' ')[1])
            games = games.split('; ')
            self.games = []
            for game in games:
                x = game.split(', ')
                rgb = [0,0,0]
                for part in x:
                    y = part.split()
                    color = y[1]
                    num = int(y[0])
                    rgb[colors[color]] = num
                self.games.append(tuple(rgb))
        def check_valid(self):
            for game in self.games:
                if any([q>w for q,w in zip(game, (12,13,14))]):
                    return False
            return True
    
    gameids = []
        
    f = open(filename, 'r')
    lines = f.readlines()
    for line in lines:
        x = game(line)
        if x.check_valid():
            gameids.append(x.gameid)
    print(sum(gameids))
import numpy as np   
def part2(filename): 
    class game():
        def __init__(self, string):
            colors = {'red':0, 'green':1, 'blue':2}
            gameid, games = string.split(': ')
            self.gameid = int(gameid.split(' ')[1])
            games = games.split('; ')
            self.games = []
            for game in games:
                x = game.split(', ')
                rgb = [0,0,0]
                for part in x:
                    y = part.split()
                    color = y[1]
                    num = int(y[0])
                    rgb[colors[color]] = num
                self.games.append(tuple(rgb))
        def find_min(self):
            arr = np.array(self.games)
            return tuple(arr.max(axis=0))
        def power(self):
            min = self.find_min()
            return np.prod(min)
    f = open(filename, 'r')
    lines = f.readlines()
    sum = 0
    for line in lines:
        sum += game(line).power()
    print(sum)

# import timeit
# repetitions = 1
# s1 = timeit.timeit("part1('input')", "from __main__ import part1", number=repetitions)
# s2 = timeit.timeit("part2('input')", "from __main__ import part2", number=repetitions)
# print(s1/repetitions)
# print(s2/repetitions)

part1('input')
part2('input')
