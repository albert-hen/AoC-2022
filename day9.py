inputfile = 'input/day9.txt'

def update(xdif, ydif):
    tx,ty = 0,0
    if xdif == 2 and ydif == 0:
        tx +=1
    if xdif == -2 and ydif == 0:
        tx -=1
    if xdif == 0 and ydif == 2:
        ty +=1
    if xdif == 0 and ydif == -2:
        ty -=1

    if xdif == 2 and ydif == -1 or xdif == 1 and ydif == -2:
        tx +=1
        ty -=1
    if xdif == -2 and ydif == -1 or xdif == -1 and ydif == -2:
        tx -=1
        ty -=1
    if xdif == -1 and ydif == 2 or xdif == -2 and ydif == 1:
        tx -=1
        ty +=1
    if xdif == 1 and ydif == 2 or xdif == 2 and ydif == 1:
        tx +=1
        ty +=1

    return (tx,ty)
    

#part 1
with open(inputfile) as f:

    lines = f.readlines()

    pairs = [(l.split()[0],int(l.split()[1])) for l in lines]

    visited = set()
    visited.add((0,0))

    dirs = {'D':(1,0), 'U':(-1,0), 'L':(0,-1), 'R':(0,1)}

    curx, cury = 0,0
    tx, ty = 0,0
    for dir, steps in pairs:
        while steps:
            steps -= 1

            dx,dy = dirs[dir]
            curx += dx
            cury += dy

            #update tail
            xdif = curx - tx
            ydif = cury - ty

            txu, tyu = update(xdif, ydif)
            tx+=txu
            ty+=tyu

            visited.add((tx,ty))

    print(len(visited))

#part 2
def update3(xdif, ydif):
    dx,dy = 0,0

    #find direction
    if xdif:
        dx = xdif//abs(xdif)
    if ydif:
        dy = ydif//abs(ydif)
    
    #only move when either dif is 2
    if abs(xdif) == 2 or abs(ydif) == 2:
        return (dx,dy)
    else:
        return (0,0)

with open(inputfile) as f:

    lines = f.readlines()
    pairs = [(l.split()[0],int(l.split()[1])) for l in lines]

    visited = set()
    visited.add((0,0))

    dirs = {'D':(1,0), 'U':(-1,0), 'L':(0,-1), 'R':(0,1)}
    knots = [[0,0] for x in range(10)]
    visited = set()
    for dir, steps in pairs:

        while steps:
            steps -= 1

            dx,dy = dirs[dir]
            knots[0][0] += dx
            knots[0][1] += dy

            for i in range(1,10):
                xdif = knots[i-1][0] - knots[i][0]
                ydif = knots[i-1][1] - knots[i][1]

                txu, tyu = update3(xdif, ydif)


                knots[i][0]+=txu
                knots[i][1]+=tyu

            visited.add((knots[9][0],knots[9][1]))
    print(len(visited))

