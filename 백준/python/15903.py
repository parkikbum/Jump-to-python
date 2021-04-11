import sys
n,m = map(int, sys.stdin.readline().split())
min1 = 0
min2 = 0
summ = 0
num = list()
num = list(map(int, sys.stdin.readline().split()))
for i in range(m):
    min1 = min(num)
    num.pop(num.index(min1))
    min2 = min(num)
    num.pop(num.index(min2))
    summ = min1 + min2
    num.append(summ)
    num.append(summ)
print(sum(num))