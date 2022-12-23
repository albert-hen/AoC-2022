infile = 'input/day18.txt'

with open(infile) as f: inp = f.readlines()

inp = [x.strip() for x in inp]
inp = [x.split(',') for x in inp]
inp = [(int(x[0]),int(x[1]),int(x[2])) for x in inp]

adj = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]

drops = set()

#part 1
surfaceArea = 0
for x,y,z in inp:

    surfaceArea += 6
    for dx,dy,dz in adj:
        if (x+dx, y+dy, z+dz) in drops:
            surfaceArea -= 2
    drops.add((x,y,z))
print(surfaceArea)

#part 2
# we run bfs within a bounded box, outside of the droplet
from collections import deque

#range of values are [0,20)
boundHi = 20
boundLo = -1

q = deque()
visited = set()
start = (-1,-1,-1)
q.append(start)
visited.add(start)

surfaceArea = 0

while q:
    #pop off queue
    x,y,z = q.popleft()

    #if touching cube then increment SA
    for dx,dy,dz in adj:

        n = (x+dx, y+dy, z+dz)
        if n in drops:
            surfaceArea += 1
        
        #explore neighbors that are not part of drop, not visited, and within bounds

        if n not in drops and n not in visited and boundLo<=n[0]<=boundHi and boundLo<=n[1]<=boundHi and boundLo<=n[2]<=boundHi:
            q.append(n)
            visited.add(n)


    



print(surfaceArea)