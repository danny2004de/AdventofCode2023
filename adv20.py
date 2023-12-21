from collections import deque
from math import lcm

def part1(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    q = deque()
    modules = {}
    broadcast_receivers = []
    inputs = {}
    for line in lines:
        line = line.split(' -> ')
        if line[0] == 'broadcaster':
            name = 'broadcaster'
            broadcast_receivers = line[1].split(', ')
            l = [None, None, broadcast_receivers]
        elif line[0][0] == '&':
            name = line[0][1:]
            l = ['&', {}, line[1].split(', ')]
            modules[name] = l
        elif line[0][0] == '%':
            name = line[0][1:]
            l = ['%', 0, line[1].split(', ')]
            modules[name] = l
        for x in l[2]:
            if x in inputs:
                inputs[x].append(name)
            else:
                inputs[x] = [name]
    for module, inputlist in inputs.items():
        if (module in modules) and (modules[module][0] == '&'):
            modules[module][1] = {x:0 for x in inputlist}
    lowcount = 0
    highcount = 0
    for i in range(1000):
        lowcount += 1
        for br in broadcast_receivers:
            q.append((br, 'broadcaster', 0))
        while len(q):
            m, name, signal = q.popleft()
            lowcount += 1 - signal
            highcount += signal
            if m not in modules:
                continue
            if modules[m][0] == '&':
                modules[m][1][name] = signal
                if all(modules[m][1].values()):
                    for n in modules[m][2]:
                        q.append((n, m, 0))
                else:
                    for n in modules[m][2]:
                        q.append((n, m, 1))
            if modules[m][0] == '%':
                if signal == 1:
                    continue
                modules[m][1] = 1 - modules[m][1]
                for n in modules[m][2]:
                        q.append((n, m, modules[m][1]))
    print(lowcount*highcount)

def part2(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    q = deque()
    modules = {}
    broadcast_receivers = []
    inputs = {}
    for line in lines:
        line = line.split(' -> ')
        if line[0] == 'broadcaster':
            name = 'broadcaster'
            broadcast_receivers = line[1].split(', ')
            l = [None, None, broadcast_receivers]
        elif line[0][0] == '&':
            name = line[0][1:]
            l = ['&', {}, line[1].split(', ')]
            modules[name] = l
        elif line[0][0] == '%':
            name = line[0][1:]
            l = ['%', 0, line[1].split(', ')]
            modules[name] = l
        for x in l[2]:
            if x in inputs:
                inputs[x].append(name)
            else:
                inputs[x] = [name]
    for module, inputlist in inputs.items():
        if (module in modules) and (modules[module][0] == '&'):
            modules[module][1] = {x:0 for x in inputlist}
    moduleswecareabout = inputs['dg']
    i = 0
    nums = []
    while len(moduleswecareabout):
        i += 1
        for br in broadcast_receivers:
            q.append((br, 'broadcaster', 0))
        while len(q):
            m, name, signal = q.popleft()
            if m == 'rx':
                continue
            if modules[m][0] == '&':
                modules[m][1][name] = signal
                if all(modules[m][1].values()):
                    for n in modules[m][2]:
                        q.append((n, m, 0))
                else:
                    for n in modules[m][2]:
                        q.append((n, m, 1))
                    if m in moduleswecareabout:
                        nums.append(i)
                        moduleswecareabout.remove(m)
            if modules[m][0] == '%':
                if signal == 1:
                    continue
                modules[m][1] = 1 - modules[m][1]
                for n in modules[m][2]:
                        q.append((n, m, modules[m][1]))
    print(lcm(*nums))
    
    
part1('input')
part2('input')