from functools import total_ordering
from functools import reduce
import random
def part1(filename):
    @total_ordering
    class hand:
        def __init__(self, string, bid):
            self.string = string
            self.cards = dict(reduce(lambda x, y: {**x, y: x.get(y, 0) + 1}, string, {}))
            self.bid = int(bid)
            self.type = 0
            k = self.cards.values()
            if 5 in k: self.type = 1
            elif 4 in k: self.type = 2
            elif 3 in k: 
                if 2 in k: self.type = 3
                else: self.type = 4
            elif 2 in k:
                if len([i for i in k if i == 2]) == 2: self.type = 5
                else: self.type = 6
            else: self.type = 7
                 
        def __eq__ (self, other):
            return self.cards == other.cards
        def __gt__(self, other):
            if self.type < other.type:
                return True
            if self.type > other.type:
                return False
            for i,j in zip(self.string, other.string):
                selfstrength = '23456789TJQKA'.index(i)
                otherstrength = '23456789TJQKA'.index(j)
                if selfstrength==otherstrength: continue
                if selfstrength > otherstrength: return True
                if selfstrength < otherstrength: return False
            return False

    f = open(filename, 'r')
    lines = f.read().splitlines()
    hands = [hand(*tuple(i.split())) for i in lines]
    hands = sorted(hands)
    sum = 0
    for i in range(len(hands)):
        rank = i+1
        sum += rank*hands[i].bid
    print(sum)
        
    
def part2(filename):
    @total_ordering
    class hand:
        def __init__(self, string, bid):
            self.string = string
            self.cards = dict(reduce(lambda x, y: {**x, y: x.get(y, 0) + 1}, string, {}))
            jokers = self.cards.pop('J', 0)
            try:
                m = max(self.cards, key=self.cards.get)
                self.cards[m] += jokers
            except:
                self.cards['2'] = 5
            self.bid = int(bid)
            self.type = 0
            k = self.cards.values()
            if 5 in k: self.type = 1
            elif 4 in k: self.type = 2
            elif 3 in k: 
                if 2 in k: self.type = 3
                else: self.type = 4
            elif 2 in k:
                if len([i for i in k if i == 2]) == 2: self.type = 5
                else: self.type = 6
            else: self.type = 7
                 
        def __eq__ (self, other):
            return self.string == other.string
        def __gt__(self, other):
            if self.type < other.type:
                return True
            if self.type > other.type:
                return False
            for i,j in zip(self.string, other.string):
                selfstrength = 'J23456789TQKA'.index(i)
                otherstrength = 'J23456789TQKA'.index(j)
                if selfstrength==otherstrength: continue
                if selfstrength > otherstrength: return True
                if selfstrength < otherstrength: return False
            return False
    f = open(filename, 'r')
    lines = f.read().splitlines()
    hands = [hand(*tuple(i.split())) for i in lines]
    hands = sorted(hands)
    sum = 0
    for i in range(len(hands)):
        rank = i+1
        sum += rank*hands[i].bid
    print(sum)
    print(hands[-1].string)
    
part2('input')