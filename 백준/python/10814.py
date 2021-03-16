import sys
import operator
n = int(sys.stdin.readline())
sol = []
for i in range(n):
    nage = sys.stdin.readline().split()
    sol.append([int(nage[0]),nage[1]])
sol = sorted(sol, key=operator.itemgetter(0))
for name,age in sol:
    print(name,age)