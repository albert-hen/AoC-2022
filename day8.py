infile = 'input/day8.txt'


with open(infile) as f:
    visibleset = set()

    lines = f.readlines()
    lines = [l.strip() for l in lines]
    
    N = len(lines)
    M = len(lines[0])
    
    for i in range(N):
        ma = -1
        for j in range(M):
            if int(lines[i][j]) > ma:
                visibleset.add((i,j))
                ma = int(lines[i][j])
        
        ma = -1
        for j in range(M-1,-1,-1):
            if int(lines[i][j]) > ma:
                visibleset.add((i,j))
                ma = int(lines[i][j])
            
    for j in range(M):
        ma = -1
        for i in range(N):
            if int(lines[i][j]) > ma:
                visibleset.add((i,j))
                ma = int(lines[i][j])
        
        ma = -1
        for i in range(M-1,-1,-1):
            if int(lines[i][j]) > ma:
                visibleset.add((i,j))
                ma = int(lines[i][j])
            
    
    print(len(visibleset))
    
def scenicScore(row, col, grid):
    up = 0
    down = 0
    left = 0
    right = 0
    
    #up
    crow = row
    while True:
        if crow != row and grid[crow][col] >= grid[row][col]:
            break
        if crow == 0:
            break
        
        crow -= 1
    up = row - crow
    
    #down
    crow = row
    while True:
        if crow != row and grid[crow][col] >= grid[row][col]:
            break
        if crow == N-1:
            break
        
        crow += 1
    down = crow - row
    
    #left
    ccol = col
    while True:
        if ccol != col and grid[row][ccol] >= grid[row][col]:
            break
        if ccol == 0:
            break
        
        ccol -= 1
    left = col - ccol
    
    #right
    ccol = col
    while True:
        if ccol != col and grid[row][ccol] >= grid[row][col]:
            break
        if ccol == M-1:
            break
        
        ccol += 1
    right = ccol - col
    return up*down*left*right
    
with open(infile) as f:
    
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    N = len(lines)
    M = len(lines[0])
    maxans = 0
    for i in range(N):
        for j in range(M):
            a = scenicScore(i,j,lines)
            maxans = max(maxans, a)
    print(maxans)
            