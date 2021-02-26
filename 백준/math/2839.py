n = int(input())
cnt = 0

while 1:
    if n == 0:
        print(cnt)
        break
    if n < 3:
        print(-1)
        break
    elif 3 < n < 5:
        print(-1)
        break
    if n%5 == 0:
        print(n//5 + cnt)
        break

    n = n - 3
    cnt = cnt + 1

