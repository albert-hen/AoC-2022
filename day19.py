infile = 'input/day19.txt'
with open(infile) as f: inp = f.readlines()

inp = [x.split() for x in inp]
inp = [[int(x[6]), int(x[12]),(int(x[18]), int(x[21])),(int(x[27]), int(x[30]))] for x in inp]

print(inp[0])