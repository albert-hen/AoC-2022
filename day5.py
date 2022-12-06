from collections import deque
inputFile = 'input/day5.txt'

#part 1
with open(inputFile) as f:
    lines = f.readlines()

    stacksLines = lines[:8]

    #create the stacks
    stacks = {n:deque() for n in range(1,10)}

    #parse the existing stacks
    for line in stacksLines:
        for stack in range(1,10):
            ind = 1 + 4*(stack-1)
            char = line[ind]
            
            if char != " ":
                stacks[stack].appendleft(char)

    #process the procedures
    procs = lines[10:]
    for p in procs:
        _, amount, _, source, _, dest = p.split()

        for i in range(int(amount)):
            sourceStack = stacks[int(source)]
            destStack = stacks[int(dest)]
            destStack.append(sourceStack.pop())

    #get the top of each stack
    print(''.join([stacks[x][-1] for x in range(1,10)]))

#part 2
with open(inputFile) as f:
    lines = f.readlines()

    stacksLines = lines[:8]

    #create the stacks
    stacks = {n:deque() for n in range(1,10)}

    #parse the existing stacks
    for line in stacksLines:
        for stack in range(1,10):
            ind = 1 + 4*(stack-1)
            char = line[ind]
            
            if char != " ":
                stacks[stack].appendleft(char)

    #process the procedures
    procs = lines[10:]
    for p in procs:
        _, amount, _, source, _, dest = p.split()

        tempstack = deque()
        sourceStack = stacks[int(source)]
        destStack = stacks[int(dest)]
        
        for i in range(int(amount)):
            tempstack.append(sourceStack.pop())

        for i in range(int(amount)):
            destStack.append(tempstack.pop())

    #get the top of each stack
    print(''.join([stacks[x][-1] for x in range(1,10)]))