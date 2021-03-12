cnt = 0
i = 0
while 1:
    n = input()
    if n == '0':
        break
    else:
        list_n = list(n)
        list_nn = list(n)
        list_nn.reverse()
        for x in list_n:
            if x == list_nn[i]:
                cnt = cnt + 1
            i = i + 1
        if cnt == len(list_n):
            print("yes")
            cnt = 0
            i = 0
        else:
            print("no")
            cnt = 0
            i = 0
