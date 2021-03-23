import sys
n = int(input())
n1 = n
bbh = []
i = 0
for x in range(1,n+1):
    bbh = list(str(x))
    for y in range(len(bbh)):
        bbh.append(int(bbh[0]))
        bbh.pop(0)
    x = x + sum(bbh)
    if x == n:
        for y in bbh:
            print(y,end='')
        sys.exit()
    i = 0
print(0)