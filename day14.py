infile = 'input/day14.txt'

def sim(obstacles, pourPoint, floory):
    curx = pourPoint[0]
    cury = pourPoint[1]

    while True:

        if cury > floory:
            return False
        if (curx,cury+1) not in obstacles:
            cury += 1
        elif (curx-1,cury+1) not in obstacles:
            curx -= 1
            cury += 1
        elif (curx+1,cury+1) not in obstacles:
            curx += 1
            cury += 1
        else:
            #all blocked final position found
            obstacles.add((curx,cury))
            return True

def simFloor(obstacles, pourPoint, floory):
    curx = pourPoint[0]
    cury = pourPoint[1]
    floory += 2
    while True:

        if (curx,cury+1) not in obstacles and cury+1 != floory:
            cury += 1
        elif (curx-1,cury+1) not in obstacles and cury+1 != floory:
            curx -= 1
            cury += 1
        elif (curx+1,cury+1) not in obstacles and cury+1 != floory:
            curx += 1
            cury += 1
        else:
            #all blocked final position found
            obstacles.add((curx,cury))
            return
            

with open(infile) as f: inp = [x.strip() for x in f.readlines()]

rockBlocks = set()
floory   = 0
for line in inp:
    pointlist = line.split(' -> ')
    pointlist = list(map(lambda x: x.split(','),pointlist))
    pointlist = [list(map(int, point)) for point in pointlist]
    
    for i, (x,y) in enumerate(pointlist[:-1]):
        nx = pointlist[i+1][0]
        ny = pointlist[i+1][1]

        movex = nx != x
        if movex:
            for xpos in range(min(nx,x),max(nx,x)+1):
                rockBlocks.add((xpos, y))
                floory = max(floory, y)

        else:
            for ypos in range(min(ny,y),max(ny,y)+1):
                rockBlocks.add((x, ypos))
                floory = max(floory, ypos)

#part 1
pourPoint = (500,0)
count = 0
obstacles = rockBlocks.copy()
while True:
    res = sim(obstacles, pourPoint, floory)
    if res:
        count+=1
    else:
        break
print(count)

#part 2
#part 1
pourPoint = (500,0)
count = 0
obstacles = rockBlocks.copy()
while True:
    res = simFloor(obstacles, pourPoint, floory)
    count+=1
    if pourPoint in obstacles:
        break
print(count)




