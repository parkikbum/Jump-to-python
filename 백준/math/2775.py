t = int(input())
for x in range(t):
    k = int(input())
    n = int(input())
    people = [int(l) for l in range(1,n+1)]
    for k in range(k):
        for v in range(n-1):
            people[v+1] = people[v] + people[v+1]
    people.reverse()
    print(people[0])