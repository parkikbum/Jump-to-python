n = int(input())
dc = []
dc2 = []
rank = []
for i in range(n):
    x,y = map(int, input().split())
    dc.append((x,y))
a = n
for k in dc:
    for j in dc:
        if k[0] > j[0]:
            if k[1] > j[1]:
                a = a - 1
    rank.append(a)
    a = 5
for v in rank:
    if rank.count(v) == 1:
        print(v,end = ' ')
    else:
        print(n-rank.count(v),end=' ')


