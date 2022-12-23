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

#simulates one rock drop, returns new highest
def simulate(chamber, shape, pushIter, highest):

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

    shapeHighest = max([y for _,y in shapeLocation])
    return max(highest, shapeHighest)

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
highest = 0
for i in range(N):

    highest = simulate(chamber, next(shapeIter), pushIter, highest)

#get highest block in tower
print(max([y for _,y in chamber]))


# part 2

# since the shapes and jet pattern is cycled, the height increase after each rock should have a cyclic pattern as well
# by printing out the height changes as a string, we observe there is a prefix (head) before a pattern emerges
# knowing the pattern, we can just do some math to calculate the height after 1 trillion rocks

def strIntSum(intStr):
    l = list(intStr)
    l = [int(x) for x in l]
   
    return sum(l)

#cycle iterators on input and shapes
shapeIter = cycle(shapes)
pushIter = cycle(inp)

N = 1000000000000
#holds tuple locations of blocks in tower
chamber = set()
highest = 0
pattern = []
pointer = 0
out = ""
for i in range(N):
    oldHighest = highest
    highest = simulate(chamber, next(shapeIter), pushIter, highest)
    
    change = highest - oldHighest

    out+=str(change)

    #check if tail is potential pattern
    for i in range(10,len(out)//2 + 1):
        #if so do the math
        if out[-1*i:] == out[:-1*i][-1*i:]:
        
        
            head = out[:-2*i]
            patternLen = i
            headLen = len(out) - 2*i
            #print(f'potential pattern len {patternLen} found in str len {len(out)}, head is {headLen}')
            pattern = out[-1*i:]

            tailLen = (N - headLen)%patternLen
            tail = pattern[:tailLen]
            

            headSum = strIntSum(head)
            patternSum = strIntSum(pattern)
            tailSum = strIntSum(tail)

            patternCount = (N-headLen)//patternLen

            print(headSum + patternCount*patternSum + tailSum)
            exit()


            


            

            

            


