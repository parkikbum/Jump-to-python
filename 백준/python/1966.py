nn = int(input())
op = []
out = []
i = 0
l = 0
cnt = 0
for x in range(nn):
    n,m = map(int, input().split())
    ms = list(map(int, input().split()))
    for k in ms:
        op.append((ms[i],i))
        i = i +1
    if len(op) == 1:
        print(cnt + 1)
        i = 0
        op = []
        continue
    while 1:
        if max(ms) == op[0][0]:
            if op[0][1] == m:
                print(cnt+1)
                i = 0
                l = 0
                cnt = 0
                op = []
                break
            else:
                op.pop(0)
                ms.pop(ms.index(max(ms)))
                cnt = cnt + 1
        else:
            op.append((op[0][0],op[0][1]))
            op.pop(0)
