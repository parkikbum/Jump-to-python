n = int(input())
i = 6
cnt = 2
bi = 6
if n == 1:
    print(n)
else:
    for x in range(2, 1000000000):
        if (n-i) > 1:
            i = i + (bi*x)
            cnt = cnt + 1
        elif (n-i) == 1:
            print(cnt)
            break
        elif (n-i) == 0:
            print(cnt)
            break
        elif (n-i) < 0:
            print(cnt)
            break

