from functools import lru_cache
from math import ceil
infile = 'input/day19.txt'
with open(infile) as f: inp = f.readlines()

inp = [x.split() for x in inp]
inp = [[int(x[6]), int(x[12]),(int(x[18]), int(x[21])),(int(x[27]), int(x[30]))] for x in inp]
# ore:ore clay:ore obs:ore clay geode:ore obs

#dfs on every decision point

maxGeo = 0

def dfs(built,time, oreBots, clayBots, obsBots, geoBots, ore, clay, obs, geo, blueprint, timeLimit = 24):
    
    oreBotCost = blueprint[0]
    clayBotCost = blueprint[1]
    obsBotCost = blueprint[2]
    geoBotCost = blueprint[3]

    if time > timeLimit:
        return

    global maxGeo

    #time travel to end with not building anything else
    timeLeft = timeLimit - time
    maxGeo = max(maxGeo, geo+(timeLeft+1)*geoBots)


    #time travel to built orebot
    if (oreBots):
        oreNeeded = oreBotCost - ore
        timeNeeded = max(ceil(oreNeeded / oreBots),0)
        dfs(built+['orebot'],
            time+timeNeeded+1, 
            oreBots+1, clayBots, 
            obsBots, geoBots, 
            ore + oreBots*(timeNeeded+1) - oreBotCost, 
            clay + clayBots*(timeNeeded+1), 
            obs + obsBots*(timeNeeded+1), 
            geo+geoBots*(timeNeeded+1), 
            blueprint, 
            timeLimit)

    #time travel to built claybot
    if (oreBots):
        oreNeeded = clayBotCost - ore
        timeNeeded = max(ceil(oreNeeded / oreBots),0)
        dfs(built+['claybot'],
            time+timeNeeded+1, 
            oreBots, clayBots+1, 
            obsBots, geoBots, 
            ore + oreBots*(timeNeeded+1) - clayBotCost,
            clay + clayBots*(timeNeeded+1), 
            obs + obsBots*(timeNeeded+1), 
            geo+geoBots*(timeNeeded+1), 
            blueprint, 
            timeLimit)
    
    #time travel to built obsbot
    if (oreBots and clayBots):
        oreNeeded = obsBotCost[0] - ore
        clayNeeded = obsBotCost[1] - clay
        timeNeeded = max(ceil(oreNeeded / oreBots), ceil(clayNeeded / clayBots),0)
        dfs(built+['osbot'],
            time+timeNeeded+1, 
            oreBots, clayBots, 
            obsBots+1, geoBots, 
            ore + oreBots*(timeNeeded+1) - obsBotCost[0], 
            clay + clayBots*(timeNeeded+1) - obsBotCost[1], 
            obs + obsBots*(timeNeeded+1), 
            geo+geoBots*(timeNeeded+1), 
            blueprint, 
            timeLimit)
    
    #time travel to built geobot    
    if (oreBots and obsBots):
        oreNeeded = geoBotCost[0] - ore
        obsNeeded = geoBotCost[1] - obs
        timeNeeded = max(ceil(oreNeeded / oreBots), ceil(obsNeeded / obsBots),0)
        dfs(built+['geobot'],
            time+timeNeeded+1, 
            oreBots, clayBots, 
            obsBots, geoBots+1, 
            ore + oreBots*(timeNeeded+1) - geoBotCost[0], 
            clay + clayBots*(timeNeeded+1), 
            obs + obsBots*(timeNeeded+1) - geoBotCost[1], 
            geo + geoBots*(timeNeeded+1), 
            blueprint, 
            timeLimit)


ans = 0
for i in range(1,4):
    maxGeo = 0
    dfs([],1,1,0,0,0,0,0,0,0,inp[i-1],timeLimit=32)
    print(f'blueprint {i} opens {maxGeo} geodes')
    ans += maxGeo*i
print(ans)

#['claybot', 'claybot', 'claybot', 'obsbot', 'claybot', 'obsbot', 'geobot', 'geobot']
    