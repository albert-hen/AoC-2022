
#part 1
inputFile = "input/day04.txt"

def contains(line):
    a,b = line.split(',')
    a1,a2 = a.split('-')
    b1,b2 = b.split('-')
    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)

    return (b1>=a1 and b2 <=a2) or (b1 <=a1 and b2>=a2)

with open(inputFile) as f:
    pairs = map(lambda x: x.strip(), f.readlines())
    print(sum(map(contains, pairs)))

#part 2

def overlaps(line):
    a,b = line.split(',')
    a1,a2 = a.split('-')
    b1,b2 = b.split('-')
    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)

    return (b2 >=a1 and b1 <= a2)

with open(inputFile) as f:
    pairs = map(lambda x: x.strip(), f.readlines())
    print(sum(map(overlaps, pairs)))