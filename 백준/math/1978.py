r = int(input())
list_n = [int(x) for x in input().split()]
cnt = 0
n=1000
a = [False,False] + [True]*(n-1)
primes=[]
for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
for y in primes:
    for l in list_n:
        if y == l:
            cnt = cnt+1
print(cnt)