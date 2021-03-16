n,k = map(int, input().split())
list_n = []
sol = []
cnt = 1
for x in range(1,n+1):
    list_n.append(x)
while list_n:
    if cnt == k:
        sol.append(list_n.pop(0))
        cnt = 1
    else:
        list_n.append(list_n.pop((0)))
        cnt = cnt+1
print('<'+', '.join(str(i) for i in sol)+'>')



