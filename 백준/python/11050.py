n,k = map(int, input().split())
nf = 1
kf = 1
nmkf =1
for a in range(1,n+1):
    nf = nf*a
for b in range(1,k+1):
    kf = kf*b
for c in range(1, n-k+1):
    nmkf = nmkf * c
print(int(nf/(kf*nmkf)))