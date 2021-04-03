import sys
n,m = map(int, sys.stdin.readline().split())
d_name = []
b_name = []
sol = []
for x in range(n):
    d_name.append(sys.stdin.readline().rstrip())
for y in range(m):
    b_name.append(sys.stdin.readline().rstrip())
sol = list(set(d_name) & set(b_name))
print(len(sol))
for i in sorted(sol):
    print(i)