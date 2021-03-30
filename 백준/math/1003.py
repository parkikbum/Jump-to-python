import sys
n = int(sys.stdin.readline())
for x in range(n):
    num1 = int(sys.stdin.readline())
    before = 1
    before1 = 0
    sum = 0
    if num1 == 0:
        print(1,0)
        continue
    elif num1 == 1:
        print(0,1)
        continue
    for x in range(num1):
        before1 = sum
        sum = sum + before
        before = before1
    print(before,sum)        