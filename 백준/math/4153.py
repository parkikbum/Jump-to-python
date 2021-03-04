import sys
while 1:
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    if a[0] == a[1] == a[2] == 0:
        break
    if a[0]*a[0] + a[1]*a[1] == a[2]*a[2]:
        print("right")
    else:
        print("wrong")