f = lambda: map(int,input().split())
n, m = f()
a = [list(f()) for _ in range(n)]
m, k = f()
b = [list(f()) for _ in range(m)]
c = [[0]*k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for h in range(m):
            c[i][j]+=a[i][h]*b[h][j]
for x in range(n): print(*c[x])