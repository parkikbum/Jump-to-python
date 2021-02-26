list_da = [int(x) for x in input().split()]
cnt = 1
i = 0
x = 0
if list_da[0] == 1:
     for a in range(8):
        if a == list_da[i]:
            i = i + 1
            cnt = cnt+1
            x = x + 1
if cnt == 8:
    print("ascending")
cnt = 1
i = 0
if list_da[0] == 8:
    list_da.reverse()
    for a in range(8):
        if a == list_da[i]:
            i = i + 1
            cnt = cnt + 1
            x = x+1
if cnt == 8:
    print("descending")
if x < 7:
    print("mixed")


