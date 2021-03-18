t = int(input())
ck = []
cnt =0
sol = []
for x in range(t):
    vps = input()
    ck = list(vps)
    if ck[0] == ')':
        sol.append("NO")
        continue
    for l in ck:
        if l =="(":
            cnt = cnt + 1
        elif cnt >=1:
            if l == ')':
                cnt = cnt -1
                continue
        if cnt == 0:
            if l == ')':
                sol.append("NO")
                cnt = -100
                break
    if cnt > 0:
        sol.append("NO")
        cnt = 0
    elif cnt == -100:
        cnt =0
        continue
    elif cnt == 0:
        sol.append("YES")
        cnt =0
for z in sol:
    print(z)


