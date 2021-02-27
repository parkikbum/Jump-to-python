import sys
t = int(sys.stdin.readline())
for x in range(t):
    x,y = map(int, sys.stdin.readline().split())
    d = y-x
    n = 2
    if d < 3:
        print(d)
    else:
        while d not in range(n*n-n+1, n*n+n+1):
            n = n + 1
        if d <= n*n:
            print(2*n-1)
        else:
            print(2*n)

