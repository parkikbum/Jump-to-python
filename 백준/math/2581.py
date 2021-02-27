m = int(input())
mm = int(input())
n=10000
a = [False,False] + [True]*(n-1)
primes=[]
primes_l = []
for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
for l in range(m,mm+1):
    for k in primes:
        if l == k:
            primes_l.append(l)
if len(primes_l) == 0:
    print(-1)
else:
    print(sum(primes_l))
    print(min(primes_l))
