import sys
def primeNum(num):
    if num == 1:
        return False
    if num == 2:
        return True
    else:
        for i in range(2, int((2*num)**0.5)+1):
            if num % i == 0:
                return False
        return True
while 1:
    cnt = 0
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in range(n+1, 2*n+1):
        if primeNum(i):
            cnt = cnt+1
    print(cnt)





