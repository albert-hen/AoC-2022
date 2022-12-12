inputfile = 'input/day11.txt'

#part 1
def getNew(op, old):
    d = {'old': old, 'ans' : 0}
    exec('ans='+op, d)
    return d['ans']

with open(inputfile) as f:
    
    rounds = 20

    monkeys = f.read().split('\n\n')
    M = len(monkeys)
    mdict = {x:dict() for x in range(M)}

    # parse input
    for m in monkeys:
        n, items,oper,div,true,false = m.split('\n')
        monkeyN = int(n[:-1].split()[1])
        itemList = list(map(int, items.split(': ')[1].split(', ')))
        monkeyTest = int(div.split()[-1])
        monkeyOp = oper.split('= ')[1]
        monkeyT = int(true.split()[-1])
        monkeyF = int(false.split()[-1])

        mdict[monkeyN]['items'] = itemList
        mdict[monkeyN]['op'] = monkeyOp
        mdict[monkeyN]['div'] = monkeyTest
        mdict[monkeyN]['t'] = monkeyT
        mdict[monkeyN]['f'] = monkeyF
        mdict[monkeyN]['inspecs'] = 0

    for round in range(rounds):

        for monkey in range(M):
            itemlist = mdict[monkey]['items']
            while itemlist:
                curitemWorry = itemlist.pop(0)
                mdict[monkey]['inspecs'] += 1

                op = mdict[monkey]['op']
                newWorry = getNew(op, curitemWorry)

                newWorry = newWorry // 3

                div = mdict[monkey]['div']

                if newWorry % div == 0:
                    tomonk = mdict[monkey]['t']
                else:
                    tomonk = mdict[monkey]['f']
                
                mdict[tomonk]['items'].append(newWorry)
        
    inspecs = [mdict[m]['inspecs'] for m in range(M)]
    inspecs.sort(reverse=True)
    print(inspecs[0]*inspecs[1])

# part 2, keep track of the values under each mod for each item
# passing around a list of 8 values for the 8 monkeys with different div tests
# runs for 45 seconds
def getNew2(op, oldlist, modlist):
    res = []
    for old, mod in zip(oldlist, modlist):
        d = {'old':old, 'mod':mod, 'ans':None}
        exec('ans = (' + op + ') % mod', d)
        res.append(d['ans'])
    return res

def modded(val, mods):
    return map(lambda x: val % x, mods)

with open(inputfile) as f:
    
    rounds = 10000

    monkeys = f.read().split('\n\n')
    M = len(monkeys)
    mdict = {x:dict() for x in range(M)}

    # parse input
    for m in monkeys:
        n, items,oper,div,true,false = m.split('\n')
        monkeyN = int(n[:-1].split()[1])
        itemList = list(map(int, items.split(': ')[1].split(', ')))
        monkeyTest = int(div.split()[-1])
        monkeyOp = oper.split('= ')[1]
        monkeyT = int(true.split()[-1])
        monkeyF = int(false.split()[-1])

        mdict[monkeyN]['items'] = itemList
        mdict[monkeyN]['op'] = monkeyOp
        mdict[monkeyN]['div'] = monkeyTest
        mdict[monkeyN]['t'] = monkeyT
        mdict[monkeyN]['f'] = monkeyF
        mdict[monkeyN]['inspecs'] = 0

    mods = [mdict[m]['div'] for m in range(M)]
    # change items to list of modded values
    for m in range(M):
        rawItems = mdict[m]['items']
        mdict[m]['items'] = [modded(x, mods) for x in rawItems]

    for round in range(rounds):
        #if not round%500: print(round)
        for monkey in range(M):
            itemlist = mdict[monkey]['items']
            while itemlist:
                curitemWorryList = itemlist.pop(0)
                mdict[monkey]['inspecs'] += 1

                op = mdict[monkey]['op']
                newWorryList = getNew2(op, curitemWorryList,mods)

                if newWorryList[monkey] == 0:
                    tomonk = mdict[monkey]['t']
                else:
                    tomonk = mdict[monkey]['f']
                
                mdict[tomonk]['items'].append(newWorryList)
        
    inspecs = [mdict[m]['inspecs'] for m in range(M)]
    inspecs.sort(reverse=True)
    print(inspecs[0]*inspecs[1])

# part 2 v2 using lcm (which is much better lol)
inputfile = 'input/day11.txt'
import math

def getNew(op, old):
    d = {'old': old, 'ans' : 0}
    exec('ans='+op, d)
    return d['ans']

with open(inputfile) as f:
    
    rounds = 10000

    monkeys = f.read().split('\n\n')
    M = len(monkeys)
    mdict = {x:dict() for x in range(M)}

    # parse input
    for m in monkeys:
        n, items,oper,div,true,false = m.split('\n')
        monkeyN = int(n[:-1].split()[1])
        itemList = list(map(int, items.split(': ')[1].split(', ')))
        monkeyTest = int(div.split()[-1])
        monkeyOp = oper.split('= ')[1]
        monkeyT = int(true.split()[-1])
        monkeyF = int(false.split()[-1])

        mdict[monkeyN]['items'] = itemList
        mdict[monkeyN]['op'] = monkeyOp
        mdict[monkeyN]['div'] = monkeyTest
        mdict[monkeyN]['t'] = monkeyT
        mdict[monkeyN]['f'] = monkeyF
        mdict[monkeyN]['inspecs'] = 0

    mods = [mdict[m]['div'] for m in range(M)]
    lcm = math.lcm(*mods)
    for round in range(rounds):

        for monkey in range(M):
            itemlist = mdict[monkey]['items']
            while itemlist:
                curitemWorry = itemlist.pop(0)
                mdict[monkey]['inspecs'] += 1

                op = mdict[monkey]['op']
                
                newWorry = getNew(op, curitemWorry) % lcm

                div = mdict[monkey]['div']

                if newWorry % div == 0:
                    tomonk = mdict[monkey]['t']
                else:
                    tomonk = mdict[monkey]['f']
                
                mdict[tomonk]['items'].append(newWorry)
        
    inspecs = [mdict[m]['inspecs'] for m in range(M)]
    inspecs.sort(reverse=True)
    print(inspecs[0]*inspecs[1])