inputFile = "input/day03.txt"

#part 1
with open(inputFile) as f:
    lines = f.readlines()
    prioritySum = 0

    for line in lines:
        n = len(line)
        leftChars = set(line[:n//2])
        rightChars = set(line[n//2:])
        inboth = list(leftChars.intersection(rightChars))[0]
        if inboth.islower():
            prioritySum += ord(inboth) - 97 + 1
        else:
            prioritySum += ord(inboth) - 65 + 27

    print(prioritySum)

#part 2

with open(inputFile) as f:
    lines = f.readlines()
    prioritySum = 0

    linecount = len(lines)
    for i in range(linecount//3):

        group = lines[i*3:(i+1)*3]        
        inall = list(set(group[0].strip()).intersection(set(group[1].strip())).intersection(set(group[2].strip())))[0]
        
        if inall.islower():
            prioritySum += ord(inall) - 97 + 1
        else:
            prioritySum += ord(inall) - 65 + 27

    print(prioritySum)