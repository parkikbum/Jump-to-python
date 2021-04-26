import sys
n = int(sys.stdin.readline())
dc = []
for i in range(n):
    w,h = map(int, sys.stdin.readline().split())
    dc.append((w,h))
for k in dc:
    rank = 1
    for j in dc:
        if k[0] < j[0] and k[1] < j[1]:
            rank =  rank + 1
    print(rank, end= " ")
