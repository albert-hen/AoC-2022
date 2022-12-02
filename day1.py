
#part 1
cmax = 0
curr = 0

with open("day_1_input.txt","r") as f:
    for line in f.readlines():
        l = line.strip()
        if l:
            cals = int(l)
            curr += cals
        else:
            cmax = max(cmax, curr)
            curr = 0

print(cmax)

#part2
import heapq
cmax = 0
curr = 0

heap = []
topN = 3
with open("day_1_input.txt","r") as f:
    for line in f.readlines():
        l = line.strip()
        if l:
            cals = int(l)
            curr += cals
        else:
            
            heapq.heappush(heap, curr)
            if len(heap) > topN:
                heapq.heappop(heap)

            curr = 0

print(sum(heap))