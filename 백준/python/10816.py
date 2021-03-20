from collections import Counter
n = int(input())
ncard = [int(x) for x in input().split()]
m = int(input())
mcard = [int(z) for z in input().split()]
cnt = 1
sol = []
ncard = Counter(ncard)
for i in mcard:
    sol.append(ncard[i])
for l in sol:
    print(l,end=' ')