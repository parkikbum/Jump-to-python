import sys
from collections import Counter
n,m,b = map(int, sys.stdin.readline().split())
ground = []
for x in range(n):
    line = sys.stdin.readline().rstrip().split()
    for i in line:
        ground.append(int(i))
min = 100000000000000
h = 0
gr = Counter(ground)
for l in range(257):
    sec = 0
    item = b
    for j in gr:
        if j>l:
            sec = sec + ((2*(j-l))*gr[j])
            item = item + ((j-l) * gr[j])
        else:
            sec = sec + ((l-j)*gr[j])
            item = item - ((l-j)*gr[j])
    if item>=0:
        if min >= sec:
            min = sec
            h = l
print(min, h)
