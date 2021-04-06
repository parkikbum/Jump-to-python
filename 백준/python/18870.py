import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
a = list(set(l[:]))
d = {}
a.sort()
for i in range(len(a)):
    d[a[i]] = i
for i in l:
    print(d[i] , end = ' ')