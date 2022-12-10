inputFile = "input/day02.txt"
#part 1
score = 0

gameValues = {
    'A':{'X':3+1,'Y':6+2,'Z':0+3},
    'B':{'X':0+1,'Y':3+2,'Z':6+3},
    'C':{'X':6+1,'Y':0+2,'Z':3+3}
    }

with open(inputFile,"r") as f:
    for line in f.readlines():
        
        n, m = line.split()
        curGameVal = gameValues[n][m]

        score+= curGameVal

print(score)

#part 1 v2
gameValues = {
    'A':{'X':3+1,'Y':6+2,'Z':0+3},
    'B':{'X':0+1,'Y':3+2,'Z':6+3},
    'C':{'X':6+1,'Y':0+2,'Z':3+3}
    }

with open(inputFile,"r") as f:
    
    gamescores = [gameValues[n][m] for n,m in map(lambda x: x.split(), f.readlines())]
    print(sum(gamescores))



#part 2
score = 0

gameValues = {
    'A':{'X':0+3,'Y':3+1,'Z':6+2},
    'B':{'X':0+1,'Y':3+2,'Z':6+3},
    'C':{'X':0+2,'Y':3+3,'Z':6+1}
    }

with open(inputFile,"r") as f:
    for line in f.readlines():
        
        n, m = line.split()

        curGameVal = gameValues[n][m]

        score+= curGameVal
print(score)