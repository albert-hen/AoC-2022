
#part 1
score = 0

shapeValues = {'X':1, 'Y':2, 'Z':3}

gameValues = {
    'A':{'X':3,'Y':6,'Z':0},
    'B':{'X':0,'Y':3,'Z':6},
    'C':{'X':6,'Y':0,'Z':3}
    }

with open("day_2_input.txt","r") as f:
    for line in f.readlines():
        
        n, m = line.split()

        curShapeVal = shapeValues[m]
        curGameVal = gameValues[n][m]

        score+= curShapeVal + curGameVal

print(score)

#part 2
score = 0

gameValues = {
    'A':{'X':0+3,'Y':3+1,'Z':6+2},
    'B':{'X':0+1,'Y':3+2,'Z':6+3},
    'C':{'X':0+2,'Y':3+3,'Z':6+1}
    }

with open("day_2_input.txt","r") as f:
    for line in f.readlines():
        
        n, m = line.split()

        curGameVal = gameValues[n][m]

        score+= curGameVal
print(score)