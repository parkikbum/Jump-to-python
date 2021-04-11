import sys
n,k = map(int, sys.stdin.readline().split())
arr = [int(x) for x in range(1, n+1)]
print("<" , end='')
cnt = 0
while 1 :
    if cnt == n:
        break
    for i in range(k-1):
        arr.append(arr.pop(0))
    if cnt == n-1:
        print(arr.pop(0), end='')
        break
    else:
        print("%s, " %(arr.pop(0)), end="")
    cnt = cnt + 1
print(">")
