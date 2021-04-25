import sys
from itertools import permutations
n,s = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().rstrip()))
for x in range(2,n+1):
    item = list(compinations(number,x))
    for x in range(len(sol)):
        