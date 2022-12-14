infile = 'input/day12.txt'

#split by comma but not by ones within lists
def split(s):

    ans = []

    if not s:
        return s

    cur = ""
    bracketCount = 0

    for c in s:
        if c == '[':
            bracketCount += 1
            cur += c
        elif c == ']':
            bracketCount -= 1
            cur += c
        elif c == ',':
            if bracketCount > 0:
                cur += c
            else:
                ans.append(cur)
                cur = ""
        else:
            cur += c
    ans.append(cur)
    return ans

# <0 correct order
# 0 equal
# >0 wrong order

def compare(a,b):
    #check if values are integer or lists

    aval = 'list' if a[0] == '[' else 'int'
    bval = 'list' if b[0] == '[' else 'int'

    if aval == 'int' and bval == 'int':
        return int(a) - int(b)

    elif aval == 'list' and bval == 'list':
        alist = split(a[1:-1])
        blist = split(b[1:-1])

        for i in range(min(len(alist), len(blist))):
            c = compare(alist[i],blist[i])
            if c == 0:
                continue
            else:
                return c
        #if we checked all values to be equal, compare by len
        if len(alist) < len(blist):
            return -1
        if len(alist) == len(blist):
            return 0
        else:
            return 1
    
    elif aval == 'int' and bval == 'list':
        return compare('[' + a + ']', b)

    elif aval == 'list' and bval == 'int':
        return compare(a, '[' + b + ']')

#part 1
with open(infile) as f: i = f.read()

pairs = [x.strip().split('\n') for x in i.split('\n\n')]

ans = 0

for i, (a,b) in enumerate(pairs):
    c = compare(a,b)
    if c <= 0:
        ans += i+1

print(ans)

#part2

from functools import cmp_to_key

packets = set()
for a,b in pairs:
    packets.add(a)
    packets.add(b)

firstDiv = '[[2]]'
secondDiv = '[[6]]'
packets.add(firstDiv)
packets.add(secondDiv)

packets = sorted(list(packets), key=cmp_to_key(compare))

print((packets.index(firstDiv) + 1) * (packets.index(secondDiv) + 1))