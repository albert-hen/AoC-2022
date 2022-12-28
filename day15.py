infile = 'input/day15.txt'

def yclear(beacondict, ylevel):
    beacons = set([beacondict[x]['beacon'][0] for x in beacondict if beacondict[x]['beacon'][1] == ylevel] )
    nots = set()
    for x,y in beacondict:
        dist = beacondict[(x,y)]['dist']

        ydif = abs(y - ylevel)
        xdif = dist - ydif

        if xdif >= 0:
            for i in range(xdif+1):
                nots.add(x+i)
                nots.add(x-i)
    
    nots = nots.difference(beacons)
    return len(nots)

def mergeSegments(segments):
    segments.sort()
    ans = []
    cursegment = segments[0].copy()

    for x,y in segments:
        if x <= cursegment[1]:
            cursegment[1] = max(cursegment[1],y)
        else:
            ans.append(cursegment)
            cursegment = [x,y]

    ans.append(cursegment)

    return ans

def yclearmax(beacondict, ylevel,maxval):
    segments = []
    for x,y in beacondict:
        dist = beacondict[(x,y)]['dist']

        ydif = abs(y - ylevel)
        xdif = dist - ydif
        
        if xdif >= 0:
            segmentStart = max(x-xdif, 0)
            segmentEnd = min(x+xdif, maxval)
            segments.append([segmentStart, segmentEnd])
    #merge segments

    return mergeSegments(segments)

#read input and place into tuples
with open(infile) as f: inp = f.read().split('\n')
inp = [x.split() for x in inp]

inp = [(x[2],x[3],x[8],x[9]) for x in inp]
inp = [list(map(lambda y: int(y.strip(":,xy=")),x)) for x in inp]

#make dict of sensors and 
beacondict = dict()
for i, (sx,sy,bx,by) in enumerate(inp):
    mdist = abs(sx-bx)+abs(sy-by)
    beacondict[(sx,sy)] = dict()
    beacondict[(sx,sy)]['dist'] = mdist
    beacondict[(sx,sy)]['beacon'] = (bx,by)


#part 1
test = 2000000
print(yclear(beacondict, test))

#part 2

maxcoor = 4_000_000
for i in range(0,maxcoor+1):
    segment = yclearmax(beacondict,i, maxcoor)
    if segment[0][1]-segment[0][0] < maxcoor:
        allnums = set(list(range(maxcoor+1)))
        for a,b in segment:
            allnums = allnums.difference(set(range(a,b+1)))
        missingX = list(allnums)[0]
        print(missingX*maxcoor + i)
        break
        
        
