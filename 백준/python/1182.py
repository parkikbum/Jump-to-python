import sys
from itertools import combinations
cnt = 0
n,s = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))

for i in range(1,n+1):
    comb = combinations(number, i)
    for k in comb:
        if sum(k) == s:
            cnt = cnt + 1 
print(cnt)