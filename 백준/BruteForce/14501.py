n = int(input())
a = []
dp = [0] *(n+1)

for x in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    dp[i+1] = max(dp[i], dp[i+1])
    if i + a[i][0] <= n:
        dp[i+a[i][0]] = max(dp[i]+a[i][1], dp[i+a[i][0]])
print(dp[n])
