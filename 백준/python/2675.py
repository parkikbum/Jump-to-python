a = int(input())
solution = []
for x in range(a):
    s = list(map(str,input().split()))
    r = int(s[0])
    del s[0]
    s = list(s[0])
    for z in s:
        solution.append(z*r)
    solution.append("\n")

for j in solution:
    print(j, end='')
