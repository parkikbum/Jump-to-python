import sys
n = int(sys.stdin.readline())
sol = []
for i in range(n):
    sol.append(int(sys.stdin.readline()))
sol.sort()
for l in sol:
    print(l)