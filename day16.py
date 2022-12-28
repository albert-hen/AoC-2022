from collections import defaultdict, deque
inputfile = 'input/day16.txt'

with open(inputfile) as f: inp = f.readlines()
inp = [x.strip().replace(',','').split() for x in inp]
inp = [(x[1], int(x[4].strip(';').split('=')[1]), x[9:]) for x in inp]

neighborTable = {x[0]:x[2] for x in inp}
flowTable = {x[0]:x[1] for x in inp}

#get important valves
def getImportantValves(neighborTable, flowTable):
    valves = set()
    for v in neighborTable:
        if v == 'AA' or flowTable[v] != 0:
            valves.add(v)
    return valves
        

#does bfs from source and returns list of distances to all other valves
def bfs(neighborTable, source):
    
    distTable = dict()
    distTable[source] = 0

    q = deque()
    q.append((source, 0))

    visited = set()
    visited.add(source)
    
    while q:
        curValve, vdist = q.popleft()

        neighbors = neighborTable[curValve]

        for n in neighbors:
            if n not in visited:
                distTable[n] = vdist + 1
                visited.add(n)
                q.append((n, vdist + 1))

    return distTable

# get directed weighted graph of non zero valves
def getDirectedTable(neighborTable, valves):
    directedTable = dict()

    for v in valves:
        distTable = bfs(neighborTable, v)
        for vtarget in valves:
            if vtarget != v:
                directedTable[(v,vtarget)] = distTable[vtarget]
    return directedTable

# given a path calculate the total pressure released at 30 minutes
def calculateReleaseTotal(path, directedTable, flowTable,t=30):
    totalRelease = 0
    cur = path[0]
    timepassed = 0
    for v in path[1:]:
        timespent = directedTable[(cur,v)] + 1
        cur = v
        timepassed += timespent
        totalRelease += flowTable[v] * (t-timepassed)
    return totalRelease

#total time spoent on given path
def calculateTimeSpent(path, directedTable):
    cur = path[0]
    timepassed = 0
    for v in path[1:]:
        timespent = directedTable[(cur,v)] + 1
        cur = v
        timepassed += timespent
    return timepassed

def backtrack(currentPath, targetValves, flowTable, directedTable, ans):
    #if over time we prune
    if calculateTimeSpent(currentPath, directedTable) > 30:
        return

    #calculate score of current path
    if len(currentPath) > 1:
        currentScore = calculateReleaseTotal(currentPath, directedTable, flowTable)
        if currentScore > ans[0]:
            ans[0] = currentScore
            ans[1] = currentPath.copy()

    for i,v in enumerate(targetValves):
        newTargetValves = targetValves[:i] + targetValves[i+1:]
        backtrack(currentPath+[v], newTargetValves, flowTable, directedTable, ans)
    
    #there are no more targets to explore so we return
    return

valves = getImportantValves(neighborTable, flowTable)
#table is is (source,dest):dist
directedTable = getDirectedTable(neighborTable, valves)

ans = [0,'listhere']
targetValves = list(valves)
targetValves.remove('AA')
backtrack(['AA'], targetValves, flowTable, directedTable, ans)
print(ans[0])
#print(ans[1])


