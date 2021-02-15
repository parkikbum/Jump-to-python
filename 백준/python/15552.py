import sys
l = int(sys.stdin.readline())
while 1:
    a,b = sys.stdin.readline().split()
    print(int(a)+int(b))
    l = l - 1
    if l ==0:
        break;

