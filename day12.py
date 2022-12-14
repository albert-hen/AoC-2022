from collections import deque
infile = 'input/day12.txt'

with open(infile) as f:
    rlines = f.readlines()

lines = [list(l.strip()) for l in rlines]
N = len(lines)
M = len(lines[0])

#part 1
S = None
E = None

for i,row in enumerate(lines):
    for j, col in enumerate(row):
        if lines[i][j] == 'S':
            S = (i,j)
            lines[i][j]='a'
        if lines[i][j] == 'E':
            E = (i,j)
            lines[i][j] = 'z'

queue = deque()
queue.append((S[0],S[1],0))
visited = set()
visited.add(S)


while queue:
    cur = queue.popleft()
    cx,cy,steps = cur
    #check if end
    if (cx,cy) == E:
        print(steps)
        break
    
    #go to neighbors
    
    for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
        newx = cx+dx
        newy = cy+dy

        if 0<=newx<N and 0<=newy<M:
            neighborHeight = lines[newx][newy]
            curHeight = lines[cx][cy]
            if ord(neighborHeight) - ord(curHeight) <= 1 and (newx,newy) not in visited:
                #we can go
                visited.add((newx,newy))
                queue.append((newx,newy, steps+1))
        
#part 2


        
lines = [list(l.strip()) for l in rlines]

E = None
starts = []
for i,row in enumerate(lines):
    for j, col in enumerate(row):
        if lines[i][j] == 'S':
            lines[i][j]='a'
        if lines[i][j] == 'E':
            E = (i,j)
            lines[i][j] = 'z'

        if lines[i][j] == 'a':
            starts.append((i,j))
ans = float('inf')
for si,sj in starts:
    queue = deque()
    queue.append((si,sj,0))
    visited = set()
    visited.add(S)

    while queue:
        cur = queue.popleft()
        cx,cy,steps = cur
        #check if end
        if (cx,cy) == E:
            ans = min(ans, steps)
            break
        
        #go to neighbors
        
        for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
            newx = cx+dx
            newy = cy+dy

            if 0<=newx<N and 0<=newy<M:
                neighborHeight = lines[newx][newy]
                curHeight = lines[cx][cy]
                if ord(neighborHeight) - ord(curHeight) <= 1 and (newx,newy) not in visited:
                    #we can go
                    visited.add((newx,newy))
                    queue.append((newx,newy, steps+1))
print(ans)