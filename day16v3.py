infile = 'input/day16.txt'
from collections import deque
from itertools import *
from tqdm import tqdm

# day 16 strategy: we first build a directed weighted clique graph of all non-zero-flow valves with the weights as shortest distance between a source and destination
#
# part 1: run a backtracking algorithm to find the order of target valves to explore
# part 2: test all possible distribution of non-zero-flow valves between me and the elephant

# returns a dist dict for the source
def bfsDists(valveDict, source):
    distDict = dict()
    q = deque()
    visited = set()

    q.append((source, 0))
    visited.add(source)

    while q:
        cur, curDist = q.popleft()
        neighbors = valveDict[cur][1]
        for n in neighbors:
            if n not in visited:
                visited.add(n)
                q.append((n, curDist+1))

                if n == 'AA' or valveDict[n][0]!=0:
                    distDict[(source, n)] = curDist+1

    return distDict

# runs bfs from each important valve: AA and non zero flow valves
# returns a dictionary holding all directed shortest path lengths between all important valves
def getShortDists(valveDict):
    allDistDict = dict()
    for source in valveDict:
        if source == 'AA' or valveDict[source][0]!=0:
            distDict = bfsDists(valveDict, source)

            allDistDict.update(distDict)
    return allDistDict

# runs backtracking dfs that prunes at maxMins=30 mins and when no more targets to explore
def backtrack(currentPath,currentMin,currentScore, valveDict, allDistDict, targetValves, ans, maxMins = 30):
    
    #check if current path takes too much time
    if currentMin > maxMins:
        return

    #check if the current pressure release score is good
    if currentScore > ans[0]:
        ans[0] = currentScore
        ans[1] = currentPath.copy()

    curValve = currentPath[-1]

    # recursively explore the next non-zero-flow valve
    # backtracks here when done exploring that path
    for i,nextValve in enumerate(targetValves):
        
        nextMin = currentMin+ allDistDict[(curValve,nextValve)] + 1
        nextScore = currentScore + valveDict[nextValve][0]* (maxMins - nextMin)
        remainingTargetValves = targetValves[:i]+targetValves[i+1:]
        backtrack(currentPath+[nextValve], nextMin, nextScore, valveDict, allDistDict, remainingTargetValves, ans, maxMins)

# used to build powerset of non-zero-flow valves, the elements are all possible subsets
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

#parse input
with open(infile) as f: inp = f.readlines()

inp = [x.replace(',','').split() for x in inp]

#dictionary of valves, their flows, and their neighbors
valveDict = dict()
#list of significant valves: non-zero-flow valves
sigValves = []

for i in inp:
    valve = i[1]
    flow = int(i[4].strip(';').split('=')[1])
    neighbors = i[9:]
    valveDict[valve] = (flow, neighbors)
    if flow !=0:
        sigValves.append(valve)

#dict of shortest paths of all important valves (nonzero flow), key:val is (source, dest):distance
allDistDict = getShortDists(valveDict)


# part 1
ans = [0,None]
backtrack(["AA"],0,0,valveDict, allDistDict, sigValves, ans, maxMins=30)
print(ans[0])

# part 2

# we fix the first of the sigValves (non-zero-flow valves) to one of the players to cut runtime in half
# we can do this because each element in he powerset has an equivalent mirror, for example:
# me:(A,B,C), elephant:(D, E) is the same as 
# me:(D, E), elephant:(A,B,C)

# we do this by excluding the first value for the set used to generate subsets for the elephant
sets = list(powerset(sigValves[1:]))
valvePool = set(sigValves)

maxans = 0

for s in tqdm(sets):
    #elephant subset
    elTargets = list(s)
    #my subset, will always include sigValves[0]
    myTargets = list(valvePool.difference(s))
    
    #holds the pressure release score for elephant subset
    elans = [0,None]
    #holds the score for my subset
    myans = [0,None]

    backtrack(
        ["AA"],
        0,
        0,
        valveDict,
        allDistDict,
        elTargets,
        elans,
        maxMins=26)

    backtrack(
        ["AA"],
        0,
        0,
        valveDict,
        allDistDict,
        myTargets,
        myans,
        maxMins=26)
    
    maxans = max(maxans, elans[0]+ myans[0])

print(maxans)
    

