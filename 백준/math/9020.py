t = int(input())
n=10000
list_ni = []
list_i = []
sol = []
a = [False,False] + [True]*(n-1)
primes=[]
for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
for x in range(t):
    num = int(input())
    if int(num/2) in primes:
        print(int(num/2), int(num/2))
        continue
    for j in range(len(primes)):
        if num//2 <= primes[j]:
            if (num - primes[j]) in primes:
                print(num - primes[j],primes[j])
                break

