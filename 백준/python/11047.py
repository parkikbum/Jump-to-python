n,k = map(int, input().split())
num = []
cnt = 0
for x in range(n):
    num.append(int(input()))
for i in reversed(range(n)):
    cnt = cnt + k//num[i]
    k = k%num[i]
print(cnt)