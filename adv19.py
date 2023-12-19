def part1(filename):
    f = open(filename, 'r')
    lines = f.read()
    workflow, parts = lines.split('\n\n')
    workflow = workflow.splitlines()
    parts = parts.splitlines()
    wfs = {}
    for w in workflow:
        name, x = w.split('{')
        x = x.split('}')[0].split(',')
        l = [tuple(i.split(':')) for i in x]
        wfs[name] = l
    ps = []
    for part in parts:
        part = part[1:-1].split(',')
        ps.append(tuple([int(x.split('=')[1]) for x in part]))
    accepted = []
    def run(p, wf):
        x,m,a,s = p
        if wf == 'A': 
            accepted.append(p)
            return
        if wf == 'R': return
        wf = wfs[wf]
        for i, w in enumerate(wf):
            if i == len(wf) - 1:
                run(p, w[0])
                return
            if eval(w[0]):
                run(p, w[1])
                return
    for p in ps:
        run(p, 'in')
    print(sum([sum(a) for a in accepted]))
    
from copy import deepcopy
def part2(filename):
    f = open(filename, 'r')
    lines = f.read()
    workflow, parts = lines.split('\n\n')
    workflow = workflow.splitlines()
    parts = parts.splitlines()
    wfs = {}
    for w in workflow:
        name, x = w.split('{')
        x = x.split('}')[0].split(',')
        l = [tuple(i.split(':')) for i in x]
        wfs[name] = l
    maximums = {'x':4000, 'm':4000, 'a':4000, 's':4000}
    minimums = {'x':1, 'm':1, 'a':1, 's':1}
    callers = {}
    for name, wf in wfs.items():
        for i, w in enumerate(wf):
            if i == len(wf)-1:
                n = w[0]
            else: n = w[1]
            if n not in callers:
                callers[n] = [name]
            elif name not in callers[n]:
                callers[n].append(name)
    def minmax(name, maxes, mins):
        diffs = list(map(lambda x,y: maxes[y] - mins[x] + 1, mins, maxes))
        if any([d < 0 for d in diffs]): return 0
        if name == 'in': 
            prod = 1
            for d in diffs:
                prod *= d
            return prod
        answer = 0
        ogmaxes = deepcopy(maxes)
        ogmins = deepcopy(mins)
        cs = callers[name]
        for c in cs:
            wf = wfs[c]
            indices = []
            for i in range(len(wf)):
                if name in wf[i]: 
                    indices.append(i)
            for index in indices:
                if index < len(wf) - 1:
                    comparison = wf[index][0]
                    if comparison[1] == '>':
                        mins[comparison[0]] = max(mins[comparison[0]], int(comparison[2:]) + 1)
                    elif comparison[1] == '<':
                        maxes[comparison[0]] = min(maxes[comparison[0]], int(comparison[2:]) - 1)
                for i in range(index-1, -1, -1):
                    comparison = wf[i][0]
                    if comparison[1] == '<':
                        mins[comparison[0]] = max(mins[comparison[0]], int(comparison[2:]))
                    elif comparison[1] == '>':
                        maxes[comparison[0]] = min(maxes[comparison[0]], int(comparison[2:]))
                answer += minmax(c, maxes, mins)
                mins = deepcopy(ogmins)
                maxes = deepcopy(ogmaxes)
        return answer
    print(minmax('A', maximums, minimums))  
            
part1('input') 
part2('input')
        
        
        

    
    