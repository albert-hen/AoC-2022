infile = 'input/day17.txt'
from itertools import cycle
from tqdm import tqdm

def islanded(shapeLocation, chamber):

    for x,y in shapeLocation:
        #if floor or another block is below
        if y-1 == 0 or (x, y-1) in chamber:
            return True

    return False

def shiftLoc(chamber, shapeLocation, direction, chamberWidth=7):

    if direction == '<':

        for x,y in shapeLocation:
            if x-1 == 0 or (x-1,y) in chamber:
                return shapeLocation
        
        return [(x-1,y) for x,y in shapeLocation]

    else:
        for x,y in shapeLocation:
            if x+1 == chamberWidth+1 or (x+1, y) in chamber:
                return shapeLocation

        return [(x+1, y) for x,y in shapeLocation]

#simulates one rock drop
def simulate(chamber, shape, pushIter):
    if chamber:
        highest = max([y for _,y in chamber])
    else:
        highest = 0

    #spawn shape
    shapeLocation = [(3+x, highest+4+y) for x,y in shape]

    while True:
        #push shape
        shapeLocation = shiftLoc(chamber, shapeLocation, next(pushIter), chamberWidth=7)
        #check if droppable
        if islanded(shapeLocation, chamber):
            break
        #drop shape
        shapeLocation = [(x,y-1) for x,y in shapeLocation]

    chamber.update(shapeLocation)

# parse input
with open(infile) as f: inp = f.read().strip()

shape0 = [(0,0),(1,0),(2,0),(3,0)]
shape1 = [(1,0),(0,1),(1,1),(2,1),(1,2)]
shape2 = [(0,0),(1,0),(2,0),(2,1),(2,2)]
shape3 = [(0,0),(0,1),(0,2),(0,3)]
shape4 = [(0,0),(0,1),(1,0),(1,1)]

shapes = [shape0, shape1, shape2, shape3, shape4]



# part 1

#cycle iterators on input and shapes
shapeIter = cycle(shapes)
pushIter = cycle(inp)

N = 2022
#holds tuple locations of blocks in tower
chamber = set()
for i in range(N):

    simulate(chamber, next(shapeIter), pushIter)

#get highest block in tower
print(max([y for _,y in chamber]))



