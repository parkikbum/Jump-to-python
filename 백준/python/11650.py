n = int(input())
sol = []
data = []
for i in range(n):
    x,y = map(int, input().split())
    data.append((x,y))
data.sort(key= lambda x: (x[0],x[1]))
for l in range(n):
    print(data[l][0],data[l][1])