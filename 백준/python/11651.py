n = int(input())
xy = []
for x in range(n):
    x,y= map(int, input().split())
    xy.append((x,y))
xy.sort(key= lambda a : (a[1] , a[0]))
for y in range(len(xy)):
    print(xy[y][0], xy[y][1])