n,m = map(int, input().split())
sol = []
card = list(map(int, input().split()))

for a in card:
    for b in card:
        if a == b:
            break
        for c in card:
            if b==c or a == c:
                break
            elif a+b+c <=m:
                sol.append(a+b+c)
print(max(sol))




