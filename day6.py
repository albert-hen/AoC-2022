inputFile = 'input/day6.txt'
#part 1
with open(inputFile) as f:
    firstPacket = 0
    line = f.readline()
    l = len(line)

    for i in range(l-4+1):
        window = line[i:i+4]
        
        if len(set(window)) == 4:
            firstPacket = i+4
            break
    print(firstPacket)

inputFile = 'input/day6.txt'

#part 2
with open(inputFile) as f:
    firstPacket = 0
    line = f.readline()
    l = len(line)

    for i in range(l-14+1):
        window = line[i:i+14]
        
        if len(set(window)) == 14:
            firstPacket = i+14
            break
    print(firstPacket)
