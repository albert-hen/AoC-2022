infile = 'input/day10.txt'
#part 1
with open(infile) as f:
    lines = f.readlines()

    cycle = 0
    x = 1

    checks = set([20,60,100,140,180,220])
    total = 0
    for line in lines:
        
        if line.strip() == 'noop':
            if cycle+1 in checks:
                total += x * (cycle+1)
            cycle += 1

        
        else:
            

            if cycle+1 in checks:
                total += x * (cycle+1)
            cycle += 1
            
            if cycle+1 in checks:
                total += x * (cycle+1)

            n = int(line.strip().split()[1])
            x += n
            cycle += 1

    print(total)

#part 2

def printpixel(cycle, x):
    duringCycle = cycle+1
    sprPos = x
    if x-1<= ((duringCycle-1)%40) <= x+1:
        print("#", end="")
    else:
        print(".", end="")
    if (duringCycle-1)%40 == 39:
        print()

with open(infile) as f:
    lines = f.readlines()

    cycle = 0
    x = 1

    for line in lines:
        
        if line.strip() == 'noop':
            
            #during noop
            printpixel(cycle, x)

            cycle += 1

        else:

            #during x update
            printpixel(cycle, x)


            cycle += 1
            
            #during x update
            printpixel(cycle, x)


            n = int(line.strip().split()[1])
            x += n
            cycle += 1

