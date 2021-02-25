import sys
a,b,v = sys.stdin.readline().split()
if (int(v)-int(b))%(int(a)-int(b)) == 0:
    print((int(v)-int(b))//(int(a)-int(b)))
else:
    print((int(v) - int(b))//(int(a) - int(b)) + 1)

