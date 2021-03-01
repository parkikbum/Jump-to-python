def primeNum(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if primeNum(i):
        print(i)
