import sys
num = []
n = sys.stdin.readline().strip()
num = list(n)
num.sort(reverse=True)
for x in num:
    print(x, end='')
