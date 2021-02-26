import sys
t = int(input())
for x in range(t):
    h,w,n = map(int, sys.stdin.readline().split())
    if n%h == 0:
        print(h*100 + n//h)
    elif n == 1:
        print(101)
    else:
        print((n%h*100) + (n//h)+1)