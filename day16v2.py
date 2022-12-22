infile = 'input/day16.txt'

with open(infile) as f: inp = f.readlines()


inp = [x.replace(',','').split() for x in inp]

valveDict = dict()

for i in inp:
    valve = i[1]
    flow = int(i[4].strip(';').split('=')[1])
    neighbors = i[9:]
    valveDict[valve] = (flow, neighbors)

def getPressureRelease(path, valveDict, mins=30):
    cur = path[0]

    totalPressure = 0

    for i, action in enumerate(path[1:]):
        timeleft = mins - (i+1)
        action = action.split()
        if len(action) == 2:
            valve = action[1]
            flow = valveDict[valve][0]
            totalPressure += flow*timeleft

    return totalPressure

#print(valveDict.keys())
#print(getPressureRelease(['AA','DD', 'O DD', 'CC', 'BB', 'O BB', 'AA', 'II', 'JJ', 'O JJ','II','AA','DD','EE','FF','GG','HH','O HH', 'GG', 'FF', 'EE', 'O EE', 'DD','CC','O CC'], valveDict))

# no work bc exponential runtime
def backtrack(currentPath, valveDict, ans, maxMin=30):
    print(currentPath)

    if len(currentPath) - 1 > maxMin:
        return

    # check current pressure release
    curScore = getPressureRelease(currentPath, valveDict, mins = maxMin)
    if curScore > ans[0]:
        ans[0] = curScore
        ans[1] = currentPath.copy()

    # explore next
    curValve = currentPath[-1].split()[-1]
    
    #if valve has flow and not opened, we try opening
    if valveDict[curValve][0] != 0 and 'O '+ curValve not in currentPath:
        backtrack(currentPath+['O '+curValve], valveDict, ans, maxMin)
    #try going to neighbors
    neighbors = valveDict[curValve][1]

    for n in neighbors:
        #if we just came from something, dont immediately go back
        if len(currentPath) > 1 and n == currentPath[-2]:
            continue
        backtrack(currentPath+[n], valveDict, ans, maxMin)





    
    

    
